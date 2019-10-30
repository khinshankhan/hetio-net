import os
from utils.common import NEO4J_HOME, node_types, edge_types

def write_node_files():
    for node_type in node_types:
        out_file_path = os.path.join(NEO4J_HOME, "import", f"{node_type}.tsv")
        if os.path.exists(out_file_path):
            continue
        print(f"Writing file for {node_type} nodes to {out_file_path}")
        command = f"echo 'id\tname\tkind' > {out_file_path}"
        os.system(command)
        command = f"grep '{node_type}' data/nodes.tsv >> {out_file_path}"
        os.system(command)

def write_edge_files():
    for edge_type in edge_types:
        out_file_path = os.path.join(NEO4J_HOME, "import", 
                f"{edge_type.replace('>', '')}.tsv")
        if os.path.exists(out_file_path):
            continue
        print(f"Writing file for {edge_type} edges to {out_file_path}")
        command = f"echo 'source\tmetaedge\ttarget' > {out_file_path}"
        os.system(command)
        command = f"grep '{edge_type}' data/edges.tsv >> {out_file_path}"
        os.system(command)
