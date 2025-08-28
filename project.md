## Project Proposal: Linking Neuronal Structure to Firing Patterns in Mouse V1

### Background and Motivation

Neurons convert synaptic input into action‑potential trains, yet the diversity of their firing patterns cannot be explained solely by ion‑channel composition.  Morphological features strongly influence electrical activity.  Computational and experimental studies show that the ratio of axonal radius to length affects spike propagation; increasing axonal length or decreasing radius causes modulated trains and intermittent failures[1].  Similarly, dendritic size and topology determine whether pyramidal neurons burst or fire tonically: only a certain range of dendritic tree sizes supports burst firing, and altering the branching pattern or total length can transform a cell from bursting to tonic firing[2].  In dopaminergic neurons, shorter dendrites and simpler dendritic architecture correlate with more irregular firing patterns, whereas larger dendritic domains and specific regional distribution of dendrites promote regular firing[3].  These examples highlight that structural features such as dendritic length, branching complexity, axon initial segment size, and the spatial distribution of arbors can modulate firing patterns.

Advances in connectomics provide nearly complete reconstructions of neurons, including soma location, axonal and dendritic arbors, and the set of synaptic outputs.  In the mouse visual cortex (V1) this connectivity has been paired with two‑photon calcium imaging data, enabling correlational studies between structure and activity.  Recent connectomics studies reveal that local wiring rules relate structure to function.  Neurons with similar response properties are more likely to be connected, and synapse strength and multiplicity increase with functional similarity, both at axonal and synaptic scales[4].  Inhibitory interneurons also follow functionally specific patterns: parvalbumin‑expressing (PV+) cells strongly inhibit pyramidal neurons that provide them with strong excitation and share their visual selectivity[5].  These findings suggest that connectivity itself can shape firing patterns.  Nevertheless, current 2‑photon data measure activity only for a limited set of neurons, whereas connectomics provides structural detail across many cells.  By correlating firing patterns with structural and connectivity features we may be able to predict functional roles based solely on morphology and connectivity and, conversely, infer connectivity properties from recorded firing patterns.  Such predictive models would accelerate connectome annotation and inform circuit simulations.

### Research Questions and Hypotheses

1. Do neurons with similar firing patterns form structural clusters? Hypothesis: neurons exhibiting similar firing patterns (e.g., regular spiking, bursting, irregular) will share common structural features such as output synapse number, axonal length, and dendritic complexity.
2. Which structural features determine how a neuron fires? Hypothesis: features including total axonal length and radius, number of output synapses, number of target cell types, axon initial segment size, soma depth, dendritic arbor length, branching patterns, and the spatial distribution of outputs (layers/regions) will correlate with firing pattern metrics (frequency, burst index, irregularity). Prior work indicates that increasing axonal length relative to diameter can cause fragmented or failed spike trains[1], while altering dendritic length or topology can shift firing from burst to tonic[2], and shorter dendritic domains in dopaminergic neurons associate with irregular firing[3].
3. Are firing patterns correlated with connectivity motifs? Local circuits in V1 display specific connectivity patterns (e.g., one‑to‑one, one‑to‑many, and many‑to‑one motifs), and neurons with similar responses are preferentially connected[4][5]. Hypothesis: neurons that serve as hubs (receiving many inputs or sending many outputs) will exhibit distinct firing patterns compared with neurons engaged in one‑to‑one motifs; for example, cells that receive many convergent inputs may fire more irregularly, whereas neurons that provide strong inhibition to many targets may show regular or bursty firing. We will examine whether connectivity motif type (including inhibitory vs. excitatory connections) predicts firing pattern metrics.

### Data Sources

- Connectomics data (V1DD) – high‑resolution electron‑microscopy reconstructions of neurons in mouse V1. The dataset includes soma location, dendritic and axonal morphology, synaptic contacts, and synaptic outputs (connection counts and partner identities). Outputs are more thoroughly proof‑read than inputs, so we will treat output connectivity as a primary feature. Features to extract include:
  - Total axonal length and average diameter.
  - Number of output synapses per neuron.
  - Number of distinct target neuron types (based on cell‑type labels).
  - Spatial distribution of synaptic outputs (layer distribution and radial distances).
  - Axon initial segment length and diameter (if available).
  - Soma depth and layer identity.
  - Dendritic arbor length, number of dendritic branches, and convex hull volume (proxy for dendritic domain).
- Two‑photon calcium imaging data – neuronal firing patterns recorded in vivo for the same volume. From fluorescence traces we will derive firing metrics:
  - Mean firing rate (Hz), peak amplitude.
  - Burst index (ratio of bursts to single spikes) or irregularity index.
  - Orientation selectivity index and preferred orientation (if available).
- Cell‑type annotations – transcriptomic labels (e.g., inhibitory subclasses such as Sst, Vip) and morphological types.

### Methods

#### 1. Feature extraction

- Morphological metrics: For each neuron we will compute morphological descriptors from the connectome. These include total axon length, number of branches, maximum branch order, number of output synapses, synaptic density per unit length, number of distinct target types, spatial distribution of outputs across cortical layers and radial distance, soma depth, dendritic arbor length, number of dendritic branches, and dendritic convex hull volume. These features are inspired by literature linking morphology to firing properties: dendritic tree size and topology influence burst firing[2], while dendritic domain size and distribution correlate with firing irregularity in dopaminergic neurons[3]. Axonal length and radius modulate spike train propagation[1].
- Firing metrics: For each neuron with two‑photon data we will extract firing rates, burst index (ratio of spikes within bursts vs isolated), irregularity (coefficient of variation of inter‑spike intervals), and orientation selectivity. We will classify neurons into firing pattern categories (e.g., tonic, bursty, irregular) based on established thresholds.
- Connectivity motif classification: Using the connectome, we will classify each neuron’s connectivity motif (e.g., one‑to‑one, one‑to‑many, many‑to‑one) by counting the number of postsynaptic and presynaptic partners. We will compute features such as the number of postsynaptic targets, the multiplicity of synapses to each target, and the distribution of postsynaptic cell types (excitatory vs. inhibitory).

#### 2. Statistical analysis

- Clustering: Cluster neurons based on firing metrics (e.g., k‑means or hierarchical clustering). For each cluster, examine structural features to identify common patterns; test whether within‑cluster feature distributions are narrower than chance.
- Correlation and regression: Compute Pearson/Spearman correlations between morphological features and continuous firing metrics (e.g., firing rate, burst index). Use linear/logistic regression or decision trees for prediction, avoiding unnecessary high‑dimensional methods.
- Within‑type analysis: For each cell type (e.g., Sst inhibitory), assess heterogeneity by correlating morphology and firing patterns within type.
- Cross‑type comparisons: Test whether different cell types share similar firing patterns and structural metrics (e.g., convergent determinants across types).

#### 3. Validation and interpretation

- Permutation tests: Shuffle firing patterns relative to structure and recompute statistics.
- Literature comparison: Compare to established relationships (e.g., dendritic domain size vs irregularity[3]; axonal length vs propagation failures[1]).
- Motif analysis validation: Test whether motif–firing relationships persist after controlling for morphology.

### Expected Outcomes and Significance

We anticipate discovering structural clusters corresponding to firing patterns.  For instance, neurons with high burst indices may have longer dendritic trees and more complex branching, consistent with models showing that burst firing requires intermediate dendritic sizes[2].  Neurons with irregular firing may have smaller dendritic domains and simpler architecture[3].  Axonal length, output synapse number, and the number of target types might predict firing rate and irregularity[1].  In addition, we expect that connectivity motifs will correlate with firing patterns: neurons engaged in one‑to‑many excitatory motifs may exhibit bursty or regular spiking, whereas neurons receiving many convergent inputs (many‑to‑one motifs) may fire more irregularly.  Inhibitory connectivity patterns may further distinguish firing classes.

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
