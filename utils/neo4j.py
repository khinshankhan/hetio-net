import csv
import os

from py2neo import Graph
from py2neo.data import Node, Relationship

from utils.common import node_types, edge_types, abbreviations

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
            LOAD CSV WITH HEADERS FROM "file:///{node_type}.tsv" AS row FIELDTERMINATOR "\\t"
            CREATE (:{node_type} {{id:row.id, name:row.name}});
            """
            self.graph.run(query)

        for edge_type in edge_types:
            print(f"Creating edges for type: {edge_type}")
            source_type = abbreviations[edge_type[0]]
            target_type = abbreviations[edge_type[-1]]
            relationship = abbreviations[edge_type[1:-1]]
            if edge_type == 'Gr>G':
                edge_type = 'GrG'
            query = f"""
            USING PERIODIC COMMIT 500
            LOAD CSV WITH HEADERS FROM "file:///{edge_type}.tsv" AS row FIELDTERMINATOR "\\t"
            MATCH (a:{source_type} {{id:row.source}})
            MATCH (b:{target_type} {{id:row.target}})
            CREATE (a)-[:{relationship}]->(b);
            """
            self.graph.run(query)

    def query_db(self, query):
        return self.graph.run(query).data()
