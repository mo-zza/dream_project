from dream_api import db
from dream_api.model.users import UserModel

class Users():
    def __init__(self, user_email:str):
        self.email = user_email

    def check_user(self):
        return db.read_database('USERS', self.email)

    def create_user(self, name:str, password:str, birth:int, phone:int, school:str, address:str):
        if self.check_user() == True:
            user_data = UserModel().build_user_model(name, self.email, password, birth, phone, school, address)
            db.create_database('USERS', user_data)
            return True
        else:
            return False

    def update_user(self, new_data:dict):
        old_data_dict = db.read_database('USERS', new_data.keys())
        user_id = db.read_database('USERS', self.email)['id']

        if user_id in old_data_dict:
            old_data = old_data_dict['user_id']
            return db.update_database('USERS', old_data, new_data)
        else:
            return False

    def delete_user(self):
        return db.delete_database('USERS', self.email)