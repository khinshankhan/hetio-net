import csv
import os

from pymongo import MongoClient


class MongoController():
    "Singleton class to control mongo db connection."

    def __init__(self):
        "Initialize variables for later usage."
        self.data_dir = os.path.join(os.getcwd(), "data")
        self.client = MongoClient('mongodb://localhost:27017/')
        self.doc = self.client.hetionet.data

    def create_db(self):
        "Populate document if it doesn't already exist."
        print("create")

    def query_db(self, query):
        "Yeet"
        print("m", query)
