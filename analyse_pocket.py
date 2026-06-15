from Bio.PDB import PDBParser
import numpy as np

def get_imidazole_center(residue):
    ring_atoms = ['CG', 'ND1', 'CD2', 'CE1', 'NE2']
    coords = []
    for name in ring_atoms:
        if name in residue:
            coords.append(residue[name].get_coord())
            
    if len(coords) < 5:
        return None
    return np.mean(coords, axis=0)

def get_heme_center(residue):
    nitrogen_atoms = ['NA', 'NB', 'NC', 'ND']
    coords = []
    for name in nitrogen_atoms:
        if name in residue:
            coords.append(residue[name].get_coord())
            
    if len(coords) < 4:
        return None
    return np.mean(coords, axis=0)

def run_analysis():
    parser = PDBParser(QUIET=True)
    files = ['1A3N.pdb', '1HHO.pdb']
    
    mapping = {
        'A': {'prox': 87, 'dist': 58, 'type': 'alpha'},
        'B': {'prox': 92, 'dist': 63, 'type': 'beta'},
        'C': {'prox': 87, 'dist': 58, 'type': 'alpha'},
        'D': {'prox': 92, 'dist': 63, 'type': 'beta'}
    }
    
    saved_widths = {'1A3N.pdb': {}, '1HHO.pdb': {}}

    print("Pocket coordinate generation tables:")

    for filename in files:
        structure = parser.get_structure('protein', filename)
        
        model = structure[0]
        
        print(f"\nData for file: {filename}")
        
        for chain_id in ['A', 'B', 'C', 'D']:
            lookup_chain = chain_id
            if chain_id not in model:
                if chain_id == 'C': lookup_chain = 'A'
                if chain_id == 'D': lookup_chain = 'B'
                print(f"  [Notice: missing chain {chain_id}, copying from chain {lookup_chain}]")
                
            chain = model[lookup_chain]
            res_nums = mapping[chain_id]
            
            prox_res = chain[(' ', res_nums['prox'], ' ')]
            prox_coords = get_imidazole_center(prox_res)
            
            dist_res = chain[(' ', res_nums['dist'], ' ')]
            dist_coords = get_imidazole_center(dist_res)
            
            theme_coords = None
            iron_coords = None
            for residue in chain:
                if 'HEM' in residue.get_resname():
                    theme_coords = get_heme_center(residue)
                    if 'FE' in residue:
                        iron_coords = residue['FE'].get_coord()
                    break

            print(f"chain {chain_id} coordinates:")
            print(f"  proximal histidine: {prox_coords}")
            print(f"  distal histidine: {dist_coords}")
            print(f"  haem ring: {theme_coords}")
            print(f"  iron atom: {iron_coords}")
            
            if prox_coords is not None and dist_coords is not None:
                width = np.linalg.norm(prox_coords - dist_coords)
                saved_widths[filename][chain_id] = width
                print(f"  pocket width: {width:.4f} A")
            print("")

    print("\nComparing baseline vs oxygen bound states:")
    
    for chain_id in ['A', 'B', 'C', 'D']:
        w_baseline = saved_widths['1A3N.pdb'].get(chain_id)
        w_bound = saved_widths['1HHO.pdb'].get(chain_id)
        subunit_type = mapping[chain_id]['type']
        
        print(f"chain {chain_id} ({subunit_type}) results:")
        if w_baseline and w_bound:
            delta = w_bound - w_baseline
            print(f"  empty baseline width: {w_baseline:.4f} A")
            print(f"  oxygen bound width: {w_bound:.4f} A")
            print(f"  total change: {delta:.4f} A")
            
            if abs(delta) >= 0.1:
                print("  result: the pocket changed shape significantly.")
            else:
                print("  result: the anchor didn't shift much.")
        print("")

if __name__ == "__main__":
    run_analysis()