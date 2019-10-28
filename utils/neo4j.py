import csv
import os
from py2neo import Graph
from py2neo.data import Node, Relationship

NEO4J_URL = "localhost:7474"
NEO4J_USERNAME = "neo4j"
NEO4J_PASSWORD = "password"
DATA_DIR = os.path.join(os.getcwd(), "data")

class Neo4jController():
    def __init__(self):
        self.graph = Graph()

    def create_db(self):
        with open(os.path.join(DATA_DIR, "nodes.tsv"), "r") as nodes_file:
            reader = csv.DictReader(nodes_file, delimiter="\t")
            for row in reader:
                self.graph.create(Node(row["kind"], id=row["id"], name=row["name"]))
        with open(os.path.join(DATA_DIR, "edges.tsv"), "r") as edges_file:
            reader = csv.DictReader(edges_file, delimiter="\t")
            for row in reader:
                # create relationships using merge
                pass

    def query_db(self, query):
        print(query)
