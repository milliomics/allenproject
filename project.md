## Project Proposal: Linking Neuronal Structure to Firing Patterns in Mouse V1

### Background and Motivation

Neurons convert synaptic input into action‑potential trains, yet the diversity of their firing patterns cannot be explained solely by ion‑channel composition. Morphological features strongly influence electrical activity. Computational and experimental studies show that the ratio of axonal radius to length affects spike propagation; increasing axonal length or decreasing radius causes modulated trains and intermittent failures [1]. Similarly, dendritic size and topology determine whether pyramidal neurons burst or fire tonically: only a certain range of dendritic tree sizes supports burst firing, and altering the branching pattern or total length can transform a cell from bursting to tonic firing [2]. In dopaminergic neurons, shorter dendrites and simpler dendritic architecture correlate with more irregular firing patterns, whereas larger dendritic domains and specific regional distribution of dendrites promote regular firing [3]. These examples highlight that structural features such as dendritic length, branching complexity, axon initial segment size, and the spatial distribution of arbors can modulate firing patterns.

Advances in connectomics provide nearly complete reconstructions of neurons, including soma location, axonal and dendritic arbors, and the set of synaptic outputs. In the mouse visual cortex (V1) this connectivity has been paired with two‑photon calcium imaging data, enabling correlational studies between structure and activity. V1 neurons exhibit the smallest receptive fields in the visual cortex [4], suggesting that local circuit structure may play a major role in shaping their firing patterns. However, current 2‑photon data measure activity only for a limited set of neurons, whereas connectomics provides structural detail across many cells. By correlating firing patterns with structural features we may be able to predict functional roles based solely on morphology and, conversely, infer connectivity properties from recorded firing patterns. Such predictive models would accelerate connectome annotation and inform circuit simulations.

### Research Questions and Hypotheses

1. Do neurons with similar firing patterns form structural clusters? Hypothesis: neurons exhibiting similar firing patterns (e.g., regular spiking, bursting, irregular) will share common structural features such as output synapse number, axonal length, and dendritic complexity.
2. Which structural features determine how a neuron fires? Hypothesis: features including total axonal length and radius, number of output synapses, number of target cell types, axon initial segment size, soma depth, dendritic arbor length, branching patterns, and the spatial distribution of outputs (layers/regions) will correlate with firing pattern metrics (frequency, burst index, irregularity). Prior work indicates that increasing axonal length relative to diameter can cause fragmented or failed spike trains [1], while altering dendritic length or topology can shift firing from burst to tonic [2], and shorter dendritic domains in dopaminergic neurons associate with irregular firing [3].
3. Are firing patterns correlated with the receptive field location? Because V1 neurons have small receptive fields and are retinotopically organized [4], neurons responding to the same visual location may share similar input statistics. Hypothesis: neurons with overlapping receptive fields will display similar firing patterns. We will restrict comparisons to neurons whose recorded receptive fields overlap, using published V1 receptive‑field coordinates if available.

### Data Sources

- Connectomics data (V1DD) — high‑resolution electron‑microscopy reconstructions of neurons in mouse V1. The dataset includes soma location, dendritic and axonal morphology, synaptic contacts, and, importantly, synaptic outputs (connection counts and partner identities). Outputs are more thoroughly proof‑read than inputs, so we will treat output connectivity as a primary feature. Features to extract include:
  - Total axonal length and average diameter.
  - Number of output synapses per neuron.
  - Number of distinct target neuron types (based on cell‑type labels).
  - Spatial distribution of synaptic outputs (layer distribution and radial distances).
  - Axon initial segment length and diameter (if available).
  - Soma depth and layer identity.
  - Dendritic arbor length, number of dendritic branches, and convex hull volume (proxy for dendritic domain).
- Two‑photon calcium imaging data — neuronal firing patterns recorded in vivo for the same volume. From fluorescence traces we will derive firing metrics:
  - Mean firing rate (Hz), peak amplitude.
  - Burst index (ratio of bursts to single spikes) or irregularity index.
  - Orientation selectivity index and preferred orientation (if available).
  - Receptive field location (visual field coordinates) and size.
- Cell‑type annotations — transcriptomic labels (e.g., inhibitory subclasses such as Sst, Vip) and morphological types.

### Methods

#### 1. Feature extraction

- Morphological metrics: For each neuron we will compute morphological descriptors from the connectome. These include total axon length, number of branches, maximum branch order, number of output synapses, synaptic density per unit length, number of distinct target types, spatial distribution of outputs across cortical layers and radial distance, soma depth, dendritic arbor length, number of dendritic branches, and dendritic convex hull volume. These features are inspired by literature linking morphology to firing properties: dendritic tree size and topology influence burst firing [2], while dendritic domain size and distribution correlate with firing irregularity in dopaminergic neurons [3]. Axonal length and radius modulate spike train propagation [1].
- Firing metrics: For each neuron with two‑photon data we will extract firing rates, burst index (ratio of spikes within bursts vs isolated), irregularity (coefficient of variation of inter‑spike intervals), and orientation selectivity. We will classify neurons into firing pattern categories (e.g., tonic, bursty, irregular) based on established thresholds.
- Receptive field alignment: Using receptive field coordinates, we will group neurons that share overlapping receptive fields (visual angle < 1°). Neurons in V1 have the smallest receptive fields in the visual cortex [4], enabling accurate grouping.

#### 2. Statistical analysis

- Clustering: We will perform clustering of neurons based on firing metrics (e.g., k‑means or hierarchical clustering). For each cluster we will examine the distribution of structural features to identify common patterns. We will test whether neurons within the same firing cluster exhibit narrower distributions of structural metrics than expected by chance.
- Correlation and regression: We will compute Pearson or Spearman correlations between individual morphological features and continuous firing metrics (e.g., firing rate, burst index). Linear regression models will be used to predict firing metrics from morphological features. Because the connectomics feature space is limited, linear models should be sufficient; we will avoid high‑dimensional methods like PCA. For categorical firing patterns we will use logistic regression or decision trees.
- Within‑type analysis: For each cell type (e.g., Sst inhibitory cells), we will investigate heterogeneity by correlating morphology and firing patterns. Observed diversity would support the hypothesis that different firing patterns can arise within the same morphological type.
- Cross‑type comparisons: We will compare whether neurons from different cell types share similar firing patterns and structural metrics. For example, if two distinct types (X and Y) have the same firing pattern and similar features (number of outputs, number of target types, neighbor population), this could indicate convergent structural determinants.

#### 3. Validation and interpretation

- Permutation tests: To assess significance, we will shuffle firing patterns relative to structural features and recalculate correlations and cluster metrics.
- Literature comparison: We will compare our findings to established relationships. For example, we will test whether increasing dendritic domain size in V1 correlates with reduced irregularity as observed in dopaminergic neurons [3] and whether greater axonal length associates with propagation failures [1].
- Receptive field control: We will verify that correlations hold within groups of neurons sharing similar receptive fields to ensure that observed relationships are not solely due to shared visual input statistics.

### Expected Outcomes and Significance

We anticipate discovering structural clusters corresponding to firing patterns. For instance, neurons with high burst indices may have longer dendritic trees and more complex branching, consistent with models showing that burst firing requires intermediate dendritic sizes [2]. Neurons with irregular firing may have smaller dendritic domains and simpler architecture [3]. Axonal length, output synapse number, and the number of target types might predict firing rate and irregularity [1].

Successfully predicting firing patterns from connectomic features would demonstrate that morphology encodes aspects of neuronal function. Conversely, if firing patterns predict certain connectivity features (e.g., neurons with high burst indices have more outputs onto inhibitory interneurons), these patterns could be used to guide proof‑reading and annotation in connectomics, reducing manual labor. Understanding structure–function relationships in V1 also informs computational models of vision and can be extended to other cortical areas.

### Future Directions

- Generalization across brain regions: Apply the framework to other sensory cortices to test whether structural determinants of firing patterns are universal or region‑specific.
- Inclusion of input connectivity: Once input connectivity is fully proof‑read, incorporate presynaptic features (number and type of inputs) to refine predictions.
- Integration with transcriptomics: Combine morphological features with gene‑expression profiles to explore how molecular identity influences both structure and firing.
- Causal validation: Use targeted optogenetic manipulations (e.g., altering dendritic geometry or synapse distribution) to test causal links between morphology and firing patterns, building on in vitro observations that dendritic size and topology control burst firing [2].

By leveraging high‑resolution connectomics and activity measurements, this project aims to bridge structure and function in the visual cortex, providing a foundation for predicting neuronal roles within circuits.

### References

1. Computational and experimental studies showing that the ratio of axonal radius to length affects spike propagation; increasing axonal length or decreasing radius leads to modulated trains and intermittent failures.
2. Research demonstrating that dendritic tree size and topology determine whether pyramidal neurons burst or fire tonically; only an intermediate range of dendritic sizes supports burst firing, and altering branching patterns or total length can transform a cell from bursting to tonic firing.
3. Findings in dopaminergic neurons showing that shorter dendrites and simpler dendritic architecture correlate with more irregular firing patterns, whereas larger dendritic domains and specific dendritic distributions promote regular firing.
4. Reports on the mouse visual cortex indicating that neurons in primary visual cortex (V1) have the smallest receptive fields among visual areas, giving them the highest spatial resolution.