## Part 2: Haemoglobin Interaction Analysis and Molecular Documentation

Voxelotor treats sickle cell anaemia by increasing the affinity of haemoglobin for oxygen, which stabilises the R state of the protein. This stabilisation prevents the transition to the T state, thereby inhibiting the polymerisation of deoxygenated haemoglobin, maintaining normal red blood cell shape, and reducing haemolysis.

Enclosed within this repository is the systematic analysis of the haemoglobin and Voxelotor interaction. The following sections detail the computational workflow developed to quantify structural dynamics.

## Computational Foundation: Data Parsing

* **What I did**: I developed custom Python scripts to parse the structural data from the 1HHO protein structure and the Voxelotor ligand.
* **How I did it**: By utilising Biopython I processed the PDB files to isolate the specific atomic and residue data required for this study.
* **Why it was needed**: Parsing was essential to strip away irrelevant structural information and isolate the specific ligand and protein data points necessary for subsequent geometric analysis.

## Structural Interrogation: Binding Site Identification

* **What I did**: I shifted my approach from calculating a general geometric centroid to programmatically identifying the exact biological binding site for Voxelotor.
* **How I did it**: I wrote a script to parse the 1HHO.pdb file, specifically instructing the system to navigate to the alpha chain and extract the coordinates of the Nitrogen (N) atom on the N-terminal Valine (Val1).
* **Why it was needed**: Voxelotor forms a covalent bond specifically with this N-terminal Valine. By isolating the coordinates of this exact residue rather than a broad pocket centroid, I ensured my docking grid is perfectly anchored to the site where the drug actually binds.

## Molecular Visualisation: 3D Binding Analysis

* **What I did**: I used PyMOL to render the 3D interaction between the Voxelotor ligand and the haemoglobin molecule.
* **How I did it**: I imported the coordinate data into PyMOL to create a visual representation of the docking process.
* **Why it was needed**: This visualisation was required to observe the docking of the drug into the haemoglobin structure in a 3D environment. It allows for the direct inspection of how the ligand occupies the binding pocket.

## Molecular Interactions Matrix and Free Energy Evaluation

* **What I did**: I condensed the raw interaction data and integrated the unified counts into an additive empirical scoring function to calculate the Gibbs free energy ($\Delta G$).
* **How I did it**: I filtered out automated software redundancy by mapping raw atomic contacts to distinct, unique residue interactions:
  * **Hydrogen Bonds**: 5 unique residues (LYS 40, LEU 48, HIS 50, HIS 77, ASP 79) condensed from 11 raw atomic lines to remove donor-acceptor inflation.
  * **Hydrophobic Interactions**: 5 unique non-polar patches (PHE 41, LYS 66, VAL 67, LEU 88, LEU 141) condensed from 10 raw contacts to resolve local spatial redundancy.
  * **Salt Bridges**: 2 unique residue-level ion pairs condensed from 4 raw entries to eliminate carboxylate double-counting.
  * **Pi-Cation Interactions**: 1 unique delocalized system (His63) condensed from 2 raw entries to accurately reflect imidazole ring electronic stabilization.
* **Why it was needed**: Automated tools overestimate binding networks by double-counting individual atom alignments. Distilling these into true molecular networks provides an accurate, non-inflated landscape. To compute the final thermodynamic driving force, these counts are evaluated using standard energy weights where $\omega_{HB} = -1.5$, $\omega_{HY} = -0.05$, $\omega_{salt} = -2.0$, and $\omega_{\pi} = -1.0$ kcal/mol:

$$\Delta G_{\text{bind}} \approx (n_{\text{HB}} \cdot \omega_{\text{HB}}) + (n_{\text{HY}} \cdot \omega_{\text{HY}}) + (n_{\text{salt}} \cdot \omega_{\text{salt}}) + (n_{\pi} \cdot \omega_{\pi})$$

$$\Delta G_{\text{bind}} \approx (5 \cdot -1.5) + (5 \cdot -0.05) + (2 \cdot -2.0) + (1 \cdot -1.0) = -12.75 \text{ kcal/mol}$$

The final calculated energy of **-12.75 kcal/mol** mathematically confirms a highly spontaneous, thermodynamically favorable binding event driving high nanomolar-range affinity.
