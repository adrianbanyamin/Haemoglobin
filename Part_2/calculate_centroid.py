from Bio.PDB import PDBParser

def get_site(f):
    p = PDBParser(QUIET=True)
    s = p.get_structure('1HHO', f)
    
    res = s[0]['A'][1]
    
    return res['N'].get_coord()

coords = get_site('1HHO.pdb')
print("Anchor point:", coords)
