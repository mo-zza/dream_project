import time

from dream_api import db
from dream_api.model.users import UserModel

class Users():
    def __init__(self, user_email:str):
        self.email = user_email

    def get_user(self):
        data_list = [lst for lst in db.read_database('Dreamer', 'USERS', self.email)]
        data = data_list[0]
        del(data['_id'])
    
        return data

    def create_user(self, name:str, password:str, birth:str, phone:str, school:str, address:str):
        user_data = UserModel().build_user_model(name, self.email, password, birth, phone, school, address)
        db.create_database('Dreamer','USERS', user_data)

    def update_user(self, new_data:str):
        update_time = time.time()
        try:
            db.update_database('Dreamer', 'USERS', self.email, update_time, new_data)
            return True
        except :
            return False

    def delete_user(self):
        return db.delete_database('Dreamer', 'USERS', self.email)