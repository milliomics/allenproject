import os
from typing import Any, Dict, List, Optional

import numpy as np
import pandas as pd

from hdmf_zarr import NWBZarrIO


def _normalize_plane_key(plane: Any) -> str:
    s = str(plane)
    return s if s.startswith("plane-") else f"plane-{s}"


def _get_rrs_from_dff_iface(dff_obj):
    """Return a RoiResponseSeries-like object with .data and .timestamps."""
    if hasattr(dff_obj, "data") and hasattr(dff_obj, "timestamps"):
        return dff_obj
    if hasattr(dff_obj, "roi_response_series") and len(dff_obj.roi_response_series) > 0:
        return next(iter(dff_obj.roi_response_series.values()))
    raise TypeError(f"Cannot resolve RoiResponseSeries from object: {type(dff_obj)}")


def _load_dff_matrix_and_time(rrs):
    """Return X (time x roi), t (time), dt (float)."""
    X = rrs.data[:]
    if X.ndim == 1:
        X = X[:, None]
    if X.shape[0] < X.shape[1]:  # ensure (time, roi)
        X = X.T
    if getattr(rrs, "timestamps", None) is not None:
        t = np.asarray(rrs.timestamps[:], dtype=float)
        if t.size != X.shape[0] and t.size > 1:
            t = np.linspace(t[0], t[-1], X.shape[0], dtype=float)
        dt = float(np.median(np.diff(t))) if t.size > 1 else np.nan
    else:
        rate = float(getattr(rrs, "rate", 0.0) or 0.0)
        dt = (1.0 / rate) if rate > 0 else np.nan
        t = np.arange(X.shape[0], dtype=float) * (dt if np.isfinite(dt) else 1.0)
    return X, t, dt


def _roi_ids_from_rrs(rrs, n_rois: int) -> np.ndarray:
    """Return an array of ROI ids if available, otherwise [0..N-1]."""
    try:
        rois = getattr(rrs, "rois", None)
        if rois is not None and hasattr(rois, "table"):
            table = rois.table
            if hasattr(table, "id") and hasattr(table.id, "data"):
                ids = np.asarray(table.id.data[:])
                if ids.size == n_rois:
                    return ids
    except Exception:
        pass
    return np.arange(n_rois, dtype=int)


def list_plane_keys(nwbfile_zarr) -> List[str]:
    return sorted([k for k in nwbfile_zarr.processing.keys() if str(k).startswith("plane-")])


def extract_traces_for_session(
    session_name: str,
    base_dir: str,
) -> Dict[str, Any]:
    """
    Load a session and extract per-plane traces and stimulus table.

    Returns a dict with:
      - session_name: str
      - stim_table: pd.DataFrame
      - planes: List[Dict] with keys:
          plane_key: str (e.g., "plane-0")
          plane_index: Optional[int]
          X: np.ndarray (T, N)
          t: np.ndarray (T,)
          dt: float
          roi_ids: np.ndarray (N,)
    """
    nwb_path_zarr = os.path.join(base_dir, session_name, f"{session_name}.nwb.zarr")
    if not os.path.exists(nwb_path_zarr):
        raise FileNotFoundError(f"NWB Zarr not found at: {nwb_path_zarr}")

    io = NWBZarrIO(nwb_path_zarr, mode="r")
    nwbfile_zarr = io.read()

    try:
        stim_table = nwbfile_zarr.intervals["stimulus_table"].to_dataframe()
    except Exception as e:
        raise RuntimeError(f"Could not read stimulus_table: {e}")

    planes_out: List[Dict[str, Any]] = []
    for plane_key in list_plane_keys(nwbfile_zarr):
        proc = nwbfile_zarr.processing[plane_key]
        if "dff" not in getattr(proc, "data_interfaces", {}):
            continue
        try:
            dff_obj = proc.data_interfaces["dff"]
            rrs = _get_rrs_from_dff_iface(dff_obj)
            X, t, dt = _load_dff_matrix_and_time(rrs)
            roi_ids = _roi_ids_from_rrs(rrs, X.shape[1])
        except Exception as e:
            # Skip a bad plane but continue others
            print(f"[skip] {plane_key}: {e}")
            continue

        # Optional numeric plane index if key is formatted as 'plane-<int>'
        try:
            plane_index = int(str(plane_key).split("-", 1)[1])
        except Exception:
            plane_index = None

        planes_out.append({
            "plane_key": str(plane_key),
            "plane_index": plane_index,
            "X": X,
            "t": t,
            "dt": float(dt),
            "roi_ids": roi_ids,
        })

    return {
        "session_name": session_name,
        "stim_table": stim_table,
        "planes": planes_out,
    }


def save_traces_npz(
    traces: Dict[str, Any],
    out_dir: str,
    prefix: Optional[str] = None,
) -> List[str]:
    """Save per-plane traces to NPZ files. Returns list of paths."""
    os.makedirs(out_dir, exist_ok=True)
    session_name = traces.get("session_name", "session")
    prefix = prefix or session_name
    paths: List[str] = []
    for p in traces.get("planes", []):
        plane_tag = p.get("plane_key", "plane")
        path = os.path.join(out_dir, f"{prefix}_{plane_tag}.npz")
        np.savez(
            path,
            X=p["X"],
            t=p["t"],
            dt=p.get("dt", np.nan),
            roi_ids=p.get("roi_ids", np.array([], int)),
            plane_key=p.get("plane_key", ""),
            plane_index=p.get("plane_index", -1),
        )
        paths.append(path)
    return paths


if __name__ == "__main__":
 
    BASE_DIR = "/Users/farah/Allen/allenproject/data/409828_V1DD_GoldenMouse"
    SESSION = "409828_2018-12-13_15-10-05_nwb_2025-08-08_16-27-52"
    OUT_DIR = "/Users/farah/Allen/allenproject/outputs"

    traces = extract_traces_for_session(SESSION, BASE_DIR)
    print(f"session: {traces['session_name']}")
    print(f"stim_table rows: {len(traces['stim_table'])}")
    print(f"planes extracted: {len(traces['planes'])}")
    for p in traces["planes"]:
        print(f" - {p['plane_key']}: X={p['X'].shape}, dt={p['dt']:.4f}s, rois={p['roi_ids'].size}")

    saved = save_traces_npz(traces, OUT_DIR, prefix=f"{SESSION}")
    print("saved:", "\n ".join(saved))


