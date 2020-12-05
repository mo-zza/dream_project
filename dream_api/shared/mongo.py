from pymongo import MongoClient


class MongoDB():
    def __init__(self, user='Admin', password='DreamsComeTrue', db_name='Dreamer'):
        self.mongo = MongoClient(f"mongodb+srv://{user}:{password}@dream-cluster.i4zfu.mongodb.net/{db_name}?retryWrites=true&w=majority")

    
    def create_database(self, db_name:str, collection_name:str, data:dict):
        db_name = self.mongo[f'{db_name}']
        collection = db_name[f'{collection_name}']

        return collection.insert_one(data)

    def update_database(self, db_name:str, collection_name:str, query_key:str, old_data:str, update_key:str, update_data:str):
        db_name = self.mongo[f'{db_name}']
        collection = db_name[f'{collection_name}']

        query = {query_key : old_data}
        new_data = {"$set" : {update_key : update_data}}

        return collection.update(query, new_data)

    def read_document(self, db_name:str, collection_name:str):
        db_name = self.mongo[f'{db_name}']
        collection = db_name[f'{collection_name}']
        collection_list = [lst for lst in collection.find()]

        return collection_list

    def read_filed(self, db_name:str, collection_name:str, search_key:str, search_item:str):
        db_name = self.mongo[f'{db_name}']
        collection = db_name[f'{collection_name}']
        query = { search_key : search_item}

        data = collection.find(query)

        data_list = [lst for lst in data]

        return data_list

    def delete_database(self, db_name:str, collection_name:str, remove_data:dict):
        db_name = self.mongo[f'{db_name}']
        collection = db_name[f'{collection_name}']

        return collection.remove(remove_data)