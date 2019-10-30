import csv
import os

import pymongo


class MongoController():
    "Singleton class to control mongo db connection."

    def __init__(self):
        "Initialize variables for later usage."
        self.data_dir = os.path.join(os.getcwd(), "data")
        self.m_client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.m_db = self.m_client["hetionet"]
        self.m_col = self.m_db["data"]

    def create_db(self):
        "Populate document if it doesn't already exist."
        # due to count() being deprecated, we need to check if document exists
        # this way instead of a mongo method
        cols = 0
        for _ in self.m_col.find().limit(1):
            cols += 1
        # early exit
        if cols != 0:
            return
        # TEST DATA
        mydict = {
            "name": "woah",
            "treat": "t",
            "palliate": "p",
            "gene": "g",
            "where": "w"
            }
        mydict2 = {
            "name": "woah",
            "treat": "tt",
            "palliate": "pp",
            "gene": "gg",
            "where": "ww"
            }
        mydict3 = {
            "name": "woah",
            "treat": "t",
            "palliate": "pp",
            "gene": "g",
            "where": "ww"
            }
        self.m_col.insert([mydict, mydict2, mydict3])

    def query_db(self, query):
        "Queries the database."
        cur = self.m_col.find({"name": query})

        cols = 0  # count return
        name = ""
        treat = []
        palliate = []
        gene = []
        where = []

        for i in cur:
            # set name if found
            name = i['name']
            # since CRD is fast, and U is slow we get data split into multiple
            # documents
            treat.append(i['treat'])
            palliate.append(i['palliate'])
            gene.append(i['gene'])
            where.append(i['where'])
            cols += 1

#         # nothing found, early exit
        if cols == 0:
            print(f'Nothing found for disease "{query}"!')
            return

        information = f'''For disease "{query}" we found the following:
Name                          : {name}
Drugs that can Treat "{query}"   : {", ".join(list(set(treat)))}
Drugs that can Palliate "{query}": {", ".join(list(set(palliate)))}
Genes that Cause "{query}"       : {", ".join(list(set(gene)))}
Where "{query}" Occurs           : {", ".join(list(set(where)))}
'''
        print(information)
