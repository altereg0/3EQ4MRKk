from pymongo import MongoClient

client = MongoClient()

""" Boilerplate file
"""


class DecoyModel(object):
    def __init__(self, decoy="decoy"):
        self.decoy = decoy
        self.mongo_id = None

    def add(self):
        # collection = db.decoy
        # decoy = collection.insert_one({'decoy': self.decoy})
        # self.mongo_id = collection.inserted_id
        pass
