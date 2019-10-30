import csv
import os

from py2neo import Graph
from py2neo.data import Node, Relationship

from utils.common import node_types, edge_types

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
        for node_type in node_types:
            print(f"Creating nodes for type: {node_type}")
            query = f"CREATE CONSTRAINT ON (n:{node_type}) ASSERT n.id is UNIQUE"
            self.graph.run(query)

            query = f"""
            USING PERIODIC COMMIT 500
            LOAD CSV WITH HEADERS FROM "file:/{node_type}.tsv" AS row FIELDTERMINATOR "\\t"
            CREATE (:{node_type} {{id:row.id, name:row.name}});
            """
            self.graph.run(query)

        # load relationships

    def query_db(self, query):
        print(query)
