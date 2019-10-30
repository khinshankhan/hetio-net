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
        # The idea is to group the diseases in such a manner that we have only
        # a single document per disease since mongo CRD operations are fast but
        # update is costly. Another benefit is that we only have one db
        # interaction in this method, so communications costs is decreased.
        # A disease should have the following structure:
        # disease = {
        #     "id": str,
        #     "name": str,
        #     "treat": [str],
        #     "palliate": [str],
        #     "gene": [str],
        #     "where": [str],
        #     }

        diseases = {}
        self.m_col.insert([disease for disease in diseases])

    def query_db(self, query):
        "Queries the database."
        cur_id = self.m_col.find({"id": query})

        cols = 0  # count return
        for _ in cur_id:
            if cols > 0:
                break
            cols += 1

        # choose which query was proper
        if cols == 0:
            cur = self.m_col.find({"name": query})
        else:
            cur_id.rewind()  # to iterate again, we need to reset cursor
            cur = cur_id

        cols = 0
        id = ""
        name = ""
        treat = []
        palliate = []
        gene = []
        where = []

        for i in cur:
            # set name and id if found
            id = i['id']
            name = i['name']
            # since CRD is fast, and U is slow we get data split into multiple
            # documents
            treat.append(i['treat'])
            palliate.append(i['palliate'])
            gene.append(i['gene'])
            where.append(i['where'])
            cols += 1

        # nothing found, early exit
        if cols == 0:
            print(f'Nothing found for disease "{query}"!')
            return

        information = f'''For disease "{query}" we found the following:
ID                            : {id}
Name                          : {name}
Drugs that can Treat "{query}"   : {", ".join(list(set(treat)))}
Drugs that can Palliate "{query}": {", ".join(list(set(palliate)))}
Genes that Cause "{query}"       : {", ".join(list(set(gene)))}
Where "{query}" Occurs           : {", ".join(list(set(where)))}
'''
        print(information)
