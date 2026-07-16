from Bio.PDB import PDBParser

def get_ligand_centroid(pdb_file, resname):
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure('complex', pdb_file)
    coords = []
    
    for model in structure:
        for chain in model:
            for residue in chain:
                if residue.get_resname() == resname:
                    for atom in residue:
                        coords.append(atom.get_coord())
    
    if not coords:
        print("Ligand not found in PDB.")
        return None
    
    n = len(coords)
    x = sum(c[0] for c in coords) / n
    y = sum(c[1] for c in coords) / n
    z = sum(c[2] for c in coords) / n
    
    return (x, y, z)

pdb_path = 'combined_complex.pdb'
ligand_name = 'UNL' 

centroid = get_ligand_centroid(pdb_path, ligand_name)

if centroid:
    print(f"Centroid at: {centroid}")
