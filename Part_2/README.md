## Part 2: Haemoglobin Interaction Analysis and Molecular Documentation

Voxelotor treats sickle cell anaemia by increasing the affinity of haemoglobin for oxygen, which stabilises the R state of the protein. This stabilisation prevents the transition to the T state, thereby inhibiting the polymerisation of deoxygenated haemoglobin, maintaining normal red blood cell shape, and reducing haemolysis.

Enclosed within this repository is the systematic analysis of the haemoglobin and Voxelotor interaction. The following sections detail the computational workflow developed to quantify structural dynamics.

## Computational Foundation: Data Parsing

* **What I did**: I developed custom Python scripts to parse the structural data from the 1HHO protein structure and the Voxelotor ligand.
* **How I did it**: By utilising Biopython I processed the PDB files to isolate the specific atomic and residue data required for this study.
* **Why it was needed**: Parsing was essential to strip away irrelevant structural information and isolate the specific ligand and protein data points necessary for subsequent geometric analysis.

## Structural Interrogation: Bidning Site Idenitification

* **What I did**: I shifted my approach from calculating a general geometric centroid to programmatically identifying the exact biological binding site for Voxelotor.
* **How I did it**: I wrote a script to parse the 1HHO.pdb file, specifically instructing the system to navigate to the alpha chain and extract the coordinates of the Nitrogen (N) atom on the N-terminal Valine (Val1).
* **Why it was needed**: Voxelotor forms a covalent bond specifically with this N-terminal Valine. By isolating the coordinates of this exact residue rather than a broad pocket centroid, I ensured my docking grid is perfectly anchored to the site where the drug actually binds.

## Molecular Visualisation: 3D Binding Analysis

* **What I did**: I used PyMOL to render the 3D interaction between the Voxelotor ligand and the haemoglobin molecule.
* **How I did it**: I imported the coordinate data into PyMOL to create a visual representation of the docking process.
* **Why it was needed**: This visualisation was required to observe the docking of the drug into the haemoglobin structure in a 3D environment. It allows for the direct inspection of how the ligand occupies the binding pocket.
