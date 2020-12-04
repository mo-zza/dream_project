from pymongo import MongoClient


class MongoDB():
    def __init__(self, user='Admin', password='DreamsComeTrue', db_name='Dreamer'):
        self.mongo = MongoClient(f"mongodb+srv://{user}:{password}@dream-cluster.i4zfu.mongodb.net/{db_name}?retryWrites=true&w=majority")

    
    def create_database(self, db_name:str, collection_name:str, data:dict):
        db_name = self.mongo[f'{db_name}']
        collection = db_name[f'{collection_name}']

        return collection.insert_one(data)

    def update_database(self, db_name:str, collection_name:str, old_data:dict, update_data:dict):
        db_name = self.mongo[f'{db_name}']
        collection = db_name[f'{collection_name}']

        return collection.update(old_data, update_data, upsert=True)

    def read_database(self, db_name:str, collection_name:str, search_data:dict):
        db_name = self.mongo[f'{db_name}']
        collection = db_name[f'{collection_name}']
        query = {"email" : search_data}
        data = [data_lst for data_lst in collection.find(query)]

        return data

    def delete_database(self, db_name:str, collection_name:str, remove_data:dict):
        db_name = self.mongo[f'{db_name}']
        collection = db_name[f'{collection_name}']

        return collection.remove(remove_data)

db = MongoDB()
result = db.read_database('Dreamer', 'USERS', 'fuck')
print(result)