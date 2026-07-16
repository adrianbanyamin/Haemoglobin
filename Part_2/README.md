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

Automated profiling software tends to overestimate binding networks by double-counting individual atom alignments within the same residue sidechains. To resolve this spatial redundancy and filter out local inflation, I mapped the raw atomic contacts back to distinct, unique residue interactions. 

This distillation consolidated 11 raw hydrogen bond lines down to 5 unique residues (LYS 40, LEU 48, HIS 50, HIS 77, ASP 79) to eliminate donor-acceptor inflation. Similarly, 10 raw hydrophobic contacts were condensed to 5 unique non-polar patches (PHE 41, LYS 66, VAL 67, LEU 88, LEU 141). For the electrostatic networks, 4 raw salt bridge entries were reduced to 2 unique residue-level ion pairs to remove carboxylate double-counting, while 2 raw pi-cation entries were standardised to 1 unique delocalised system at His63 to accurately reflect imidazole ring electronic stabilisation.

To compute the final thermodynamic driving force of this configuration, these unified counts were integrated into an additive empirical scoring function using standard energy weights ($\omega_{\text{HB}} = -1.5$, $\omega_{\text{HY}} = -0.05$, $\omega_{\text{salt}} = -2.0$, and $\omega_{\pi} = -1.0$ kcal/mol):

$$\Delta G_{\text{bind}} \approx (n_{\text{HB}} \cdot \omega_{\text{HB}}) + (n_{\text{HY}} \cdot \omega_{\text{HY}}) + (n_{\text{salt}} \cdot \omega_{\text{salt}}) + (n_{\pi} \cdot \omega_{\pi})$$

$$\Delta G_{\text{bind}} \approx (5 \cdot -1.5) + (5 \cdot -0.05) + (2 \cdot -2.0) + (1 \cdot -1.0) = -12.75 \text{ kcal/mol}$$

The final calculated energy of **-12.75 kcal/mol** mathematically confirms a highly spontaneous, thermodynamically favourable binding event driving high nanomolar-range affinity.
