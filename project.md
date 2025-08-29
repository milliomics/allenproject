## Project Proposal: Linking Neuronal Structure to Firing Patterns in Mouse V1

**Keywords**: structure–function, morphology, connectomics, firing activity (spikes/hour), dendritic topology, axonal length, axon initial segment, synapse spatial targeting (spine/shaft/soma, layer), V1 (primary visual cortex), two‑photon calcium imaging (6 Hz), pupil diameter, orientation/direction selectivity (OSI/DSI), suppression index, clustering, regression, permutation tests

### Background and Motivation

Neurons convert synaptic input into action‑potential trains, yet the diversity of their firing patterns cannot be explained solely by ion‑channel composition.  Morphological features strongly influence electrical activity.  Computational and experimental studies show that the ratio of axonal radius to length affects spike propagation; increasing axonal length or decreasing radius causes modulated trains and intermittent failures[1].  Similarly, dendritic size and topology determine whether pyramidal neurons burst or fire tonically: only a certain range of dendritic tree sizes supports burst firing, and altering the branching pattern or total length can transform a cell from bursting to tonic firing[2].  In dopaminergic neurons, shorter dendrites and simpler dendritic architecture correlate with more irregular firing patterns, whereas larger dendritic domains and specific regional distribution of dendrites promote regular firing[3].  These examples highlight that structural features such as dendritic length, branching complexity, axon initial segment size, and the spatial distribution of arbors can modulate firing patterns.

Advances in connectomics provide nearly complete reconstructions of neurons, including soma location, axonal and dendritic arbors, and the set of synaptic outputs.  In the mouse visual cortex (V1) this connectivity has been paired with two‑photon calcium imaging data, enabling correlational studies between structure and activity.  Recent connectomics studies reveal that local wiring rules relate structure to function.  Neurons with similar response properties are more likely to be connected, and synapse strength and multiplicity increase with functional similarity, both at axonal and synaptic scales[4].  Inhibitory interneurons also follow functionally specific patterns: parvalbumin‑expressing (PV+) cells strongly inhibit pyramidal neurons that provide them with strong excitation and share their visual selectivity[5].  These findings suggest that connectivity itself can shape firing patterns.  Nevertheless, current 2‑photon data measure activity only for a limited set of neurons, whereas connectomics provides structural detail across many cells.  By correlating firing patterns with structural and connectivity features we may be able to predict functional roles based solely on morphology and connectivity and, conversely, infer connectivity properties from recorded firing patterns.  Such predictive models would accelerate connectome annotation and inform circuit simulations.

### Research Questions and Hypotheses

1. **Do neurons with similar firing activity (spikes/hour) form structural clusters?** Hypothesis: neurons exhibiting high versus low activity (e.g., ≥180 spikes/hour vs. ≤20 spikes/hour) will differ in structural features such as dendritic complexity and synaptic targeting. Because two‑photon calcium imaging is slow (≈6 Hz) and poorly suited to detect true bursts, we will focus on activity rate and coarse activity patterns rather than burst metrics. We will first profile activity across all imaged neurons (not only co‑registered ones), ignoring stimulus conditions, to identify recurring activity patterns. Then, for co‑registered subsets, we will map these patterns onto conditions (e.g., running vs. stationary, full‑field vs. small‑window stimuli) and existing behavioral/visual metrics (pupil diameter, OSI/DSI, suppression index).

2. **Which structural and synaptic features determine activity levels?** Hypothesis: dendritic length and topology (and related morphological descriptors) modulate whether neurons exhibit higher or lower spikes/hour, consistent with prior work showing dendritic changes can shift firing from burst‑like to tonic regimes[2]. Additional connectivity‑level features will include the spatial placement of synapses: for higher‑activity neurons we expect a larger fraction of excitatory synapses on spines (and in specific layers/compartments), whereas inhibitory‑targeted cells may show more shaft/somatic inhibitory synapses and distinct laminar distributions. We will test relationships between spikes/hour and: total axonal length/radius, counts of outputs/targets, AIS size, soma depth, dendritic arbor length/branching, and synapse spatial targeting (spine vs. shaft/soma, distance to soma, layer).

Note: A broader analysis of abstract connectivity motifs (e.g., one‑to‑one or hub‑like patterns) is lower priority here, as small numbers of connected pairs may have limited interpretability for the present aims.

### Data Sources

- Connectomics data (V1DD) – high‑resolution electron‑microscopy reconstructions of neurons in mouse V1. The dataset includes soma location, dendritic and axonal morphology, synaptic contacts, and synaptic outputs (connection counts and partner identities). Outputs are more thoroughly proof‑read than inputs, so we will treat output connectivity as a primary feature. Features to extract include:
  - Total axonal length and average diameter.
  - Number of output synapses per neuron.
  - Number of distinct target neuron types (based on cell‑type labels).
  - Spatial distribution of synaptic outputs (layer distribution, radial distances, distance to soma) and compartment targeting (spine vs. shaft/soma).
  - Axon initial segment length and diameter (if available).
  - Soma depth and layer identity.
  - Dendritic arbor length, number of dendritic branches, and convex hull volume (proxy for dendritic domain).
- Two‑photon calcium imaging data – neuronal activity recorded in vivo for overlapping volumes. Given slow sampling (≈6 Hz) and calcium kinetics, we will emphasize spikes/hour (activity rate proxies) over burst metrics, and analyze all imaged neurons (not only co‑registered). Additional features available from existing pipelines/advisors include pupil diameter, OSI/DSI, and suppression index.
- Cell‑type annotations – transcriptomic labels (e.g., inhibitory subclasses such as Sst, Vip) and morphological types.

### Methods

#### 1. Feature extraction

- Morphological metrics: total axonal length/radius, branch counts, maximum branch order, output synapse counts, synaptic density per unit length, number of distinct target types, layer/radial distributions, soma depth, dendritic arbor length/branching, and dendritic convex hull volume.
- Activity metrics from two‑photon: spikes/hour (activity rate proxies) per neuron; initially ignore stimulus conditions and profile activity across all imaged neurons to discover activity patterns; later, for co‑registered subsets, relate activity to running, full‑field vs. small‑window stimuli, pupil diameter, OSI/DSI, and suppression index. Given 6 Hz sampling, we will not rely on burst indices.
- Synapse spatial targeting: for each neuron, quantify the compartmental distribution of synapses (spine vs. shaft/soma), laminar placement, and distances to soma; summarize excitatory vs. inhibitory targeting where available.

#### 2. Statistical analysis

- Clustering: Identify activity classes from spikes/hour using k‑means/GMM; use thresholds (e.g., ≥180 vs. ≤20 spikes/hour) as anchors for “high/low” activity groups.
- Correlation and regression: Relate spikes/hour to structural and synapse‑spatial features (Pearson/Spearman, linear/logistic regression). Include laminar/compartment predictors (spine vs. shaft/soma) and distances.
- Within‑type analysis: For each transcriptomic/morphological type, assess heterogeneity in activity vs. structure/synapse placement.
- Cross‑type comparisons: Test whether distinct types converge to similar activity–structure relationships.

#### 3. Validation and interpretation

- Permutation tests: Shuffle firing patterns relative to structure and recompute statistics.
- Literature comparison: Compare to established relationships (e.g., dendritic domain size vs irregularity[3]; axonal length vs propagation failures[1]).
- Motif analysis validation: Test whether motif–firing relationships persist after controlling for morphology.

### Expected Outcomes and Significance

We expect to discover activity‑defined clusters (high vs. low spikes/hour and intermediate patterns) and corresponding structural/synaptic correlates. For example, higher‑activity neurons may exhibit longer/more complex dendritic trees and characteristic excitatory synapse placement (spine‑rich, specific layers), whereas lower‑activity neurons may align with different synapse compartment/laminar profiles. Axonal length, output synapse number, and target diversity may further predict activity levels. After initial, stimulus‑agnostic profiling, mapping co‑registered neurons back to conditions (running, full‑field vs. small‑window) and behavioral/visual metrics (pupil, OSI/DSI, suppression index) will test contextual modulation of these activity patterns.

Successfully predicting firing patterns from connectomic features would demonstrate that morphology and connectivity encode aspects of neuronal function.  Conversely, if firing patterns predict certain connectivity features (e.g., neurons with high burst indices have more outputs onto inhibitory interneurons or form specific one‑to‑many motifs), these patterns could be used to guide proof‑reading and annotation in connectomics, reducing manual labor.  Understanding structure–function relationships in V1 also informs computational models of vision and can be extended to other cortical areas.

### Future Directions

- Generalization across brain regions: Apply the framework to other sensory cortices to test whether structural determinants of firing patterns are universal or region‑specific.
- Inclusion of input connectivity: Once input connectivity is fully proof‑read, incorporate presynaptic features (number and type of inputs) to refine predictions.
- Integration with transcriptomics: Combine morphological features with gene‑expression profiles to explore how molecular identity influences both structure and firing.
- Causal validation: Use targeted optogenetic manipulations (e.g., altering dendritic geometry or synapse distribution) to test causal links between morphology and firing patterns, building on in vitro observations that dendritic size and topology control burst firing[2].

By leveraging high‑resolution connectomics and activity measurements, this project aims to bridge structure and function in the visual cortex, providing a foundation for predicting neuronal roles within circuits.

### References

1. Ofer, N., Shefi, O., & Yaari, G. (2017). Branching morphology determines signal propagation dynamics in neurons. Scientific Reports, 7, 8877. https://doi.org/10.1038/s41598-017-09184-3
2. van Elburg, R. A. J., & van Ooyen, A. (2010). Impact of dendritic size and dendritic topology on burst firing in pyramidal cells. PLoS Computational Biology, 6(5), e1000781. https://doi.org/10.1371/journal.pcbi.1000781
3. Montero, T., Gatica, R. I., Farassat, N., Meza, R., González‑Cabrera, C., Roeper, J., & Henny, P. (2021). Dendritic architecture predicts in vivo firing pattern in mouse ventral tegmental area and substantia nigra dopaminergic neurons. Frontiers in Neural Circuits, 15, 769342. https://doi.org/10.3389/fncir.2021.769342
4. Ding, Z., Fahey, P. G., Papadopoulos, S., et al. (2025). Functional connectomics reveals general wiring rule in mouse visual cortex. Nature, 640(8058), 459–469. https://doi.org/10.1038/s41586-025-08840-3
5. Znamenskiy, P., Kim, M.-H., Muir, D. R., Iacaruso, M. F., Hofer, S. B., & Mrsic-Flogel, T. D. (2024). Functional specificity of recurrent inhibition in visual cortex. Neuron, 112(6), 991–1000.e8. https://doi.org/10.1016/j.neuron.2023.12.013
