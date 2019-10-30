NEO4J_HOME = "/usr/share/java/neo4j" # can vary based on system

node_types = ["Compound", "Disease", "Gene", "Anatomy"]
edge_types = ["CrC", "CtD", "CpD", "CuG", "CbG", "CdG", "DrD", "DuG", "DaG",
        "DdG", "DlA", "AuG", "AeG", "AdG", "Gr>G", "GcG", "GiG"]
abbreviations = {"C": "Compound", "D": "Disease", "G": "Gene", "A": "Anatomy",
        "r": "resembles", "t": "treats", "p": "pilliates",
        "u": "upregulates", "d": "downregulates", "b": "binds",
        "a": "associates", "l": "localizes", "e": "expresses",
        "r>": "regulates", "c": "covaries", "i": "interacts"}
