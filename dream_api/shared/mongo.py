from pymongo import MongoClient


class MongoDB():
    def __init__(self, user, password, db_name):
        self.db = MongoClient("mongodb+srv://{user}:{password}@dream-cluster.i4zfu.mongodb.net/{db_name}?retryWrites=true&w=majority")

    
    def create_database(self, document_name:str, data:dict):
        collection = self.db.Dreamer
        document = collection.document_name

        return document.insert_one(data)

    def update_database(self, document_name:str, old_data:dict, update_data:dict):
        collection = self.db.Dreamer
        document = collection.documnet_name

        return document.update(old_data, update_data, upsert=True)

    def read_database(self, document_name:str, search_data:dict):
        collection = self.db.Dreamer
        document = collection.document_name

        return document.find_one(search_data)

    def delete_database(self, document_name:str, remove_data:dict):
        collection = self.db.Dreamer
        document = collection.document_name

        return document.remove(remove_data)
