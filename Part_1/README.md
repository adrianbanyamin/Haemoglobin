# Haemoglobin Structural Dynamics Analysis

**This repository contains the computational pipeline developed to quantify the conformational transition of haemoglobin upon oxygen binding. By processing PDB structural data, this project maps the precise sub-angstrom movements within the haem pocket, providing a quantitative bridge between static crystal structures and dynamic biophysical transitions.**

## **Project Scope**

**The objective of this analysis is to determine the extent of structural contraction in the haem pocket when comparing the deoxyhaemoglobin (T-state) baseline to the oxyhaemoglobin (R-state) configuration.**

## **Computational Methodology**

**The analysis was performed using Biopython to parse structural coordinate data from the following PDB files:**
* **1A3N.pdb: Deoxyhaemoglobin (Baseline)**
* **1HHO.pdb: Oxyhaemoglobin (Oxygen-bound)**

## **Data Engineering Routine**

**A significant challenge addressed during development involved the incomplete coordinate data in the 1HHO.pdb file, which only explicitly records chains A and B. To resolve this, a dynamic routine was implemented to:**
* **Parse the file structure to identify missing subunits.**
* **Synthesise coordinate data for the C and D chains using the protein’s internal symmetry relationships.**
* **Ensure a complete tetrameric analysis was achieved despite gaps in the raw structural data.**

## **Geometric Extraction**

**The pipeline calculates precise 3D centroids to represent the pocket’s geometry:**
* **Proximal Histidine Centre: Calculated from the mean coordinate position of five atoms (CG, ND1, CD2, CE1, NE2).**
* **Distal Histidine Centre: Computed via coordinate extraction of the relevant imidazole ring atoms.**
* **Haem Ring Centre: Derived from the mean position of the four nitrogen atoms (NA, NB, NC, ND).**
* **Iron (FE) Atom: Direct 3D coordinate mapping.**

## **Analysis and Results**

**The pipeline calculates the 3D Euclidean distance between the proximal and distal histidine centres. By comparing the bound state against the deoxy-baseline, the script identifies significant structural contractions.**

| Chain | Subunit Type | Displacement ($\Delta$ Å) | Result Significance |
| :--- | :--- | :--- | :--- |
| A | Alpha | -0.0995 | Below threshold |
| B | Beta | -0.2707 | Significant contraction |
| C | Alpha | -0.3724 | Significant contraction |
| D | Beta | -0.1931 | Significant contraction |

**These results illustrate the mechanical linkage involved in the T-to-R transition, where the iron ion’s transition to a low-spin state pulls the proximal histidine, facilitating the quaternary shift of the tetramer.**

## **Usage**

**To execute the analysis on your local machine, ensure you have the Bio library installed and the necessary .pdb files in your working directory. Run the script via:**

```bash
python analyse_pocket.py
