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

    def clear_db(self):
        self.graph.delete_all()

    def create_db(self):
        labels = ["Compound", "Disease", "Gene", "Anatomy"]
        for label in labels:
            query = f"CREATE CONSTRAINT ON (n:{label} ASSERT n.id is UNIQUE)"

        query = """
        USING PERIODIC COMMIT 5000
        LOAD CSV WITH HEADERS FROM "file:/nodes.tsv" AS row FIELDTERMINATOR "\\t"
        CREATE ({id:row.id, name:row.name, kind:row.kind});
        """
        self.graph.run(query)

        for label in labels:
            query = f"MATCH (n) WHERE n.kind = '{label}' SET n:{label}"
            self.graph.run(query)

        # load relationships

    def query_db(self, query):
        print(query)
