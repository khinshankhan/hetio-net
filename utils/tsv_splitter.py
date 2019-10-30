import os

NEO4J_HOME = "/usr/share/java/neo4j" # can vary based on system

node_types = ["Compound", "Disease", "Gene", "Anatomy"]
edge_types = ["CrC", "CtD", "CpD", "CuG", "CbG", "CdG", "DrD", "DuG", "DaG",
        "DdG", "DlA", "AuG", "AeG", "AdG", "Gr>G", "GcG", "GiG"]

def write_node_files():
    for node_type in node_types:
        out_file_path = os.path.join(NEO4J_HOME, "import", f"{node_type}.tsv")
        print(f"Writing file for {node_type} nodes to {out_file_path}")
        command = f"echo 'id\tname\tkind' > {out_file_path}"
        os.system(command)
        command = f"grep {node_type} data/nodes.tsv >> {out_file_path}"
        os.system(command)

def write_edge_files():
    for edge_type in edge_types:
        out_file_path = os.path.join(NEO4J_HOME, "import", 
                f"{edge_type.replace('>', '')}.tsv")
        print(f"Writing file for {edge_type} edges to {out_file_path}")
        command = f"echo 'source\tmetaedge\ttarget' > {out_file_path}"
        os.system(command)
        command = f"grep {edge_type} data/edges.tsv >> {out_file_path}"
        os.system(command)
