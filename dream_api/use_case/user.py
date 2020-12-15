import time

from dream_api import db
from dream_api.model.users import UserModel

class Users():
    def __init__(self, user_email:str):
        self.email = user_email

    def check_user(self):
        user_info = db.read_filed('', '', '', self.email)
        
        if user_info == []:
            return None
        else:
            return user_info

    def get_wallet_info(self):
        all_wallet = db.read_filed('', '', '', False)
        unspec_wallet = all_wallet[0]

        return unspec_wallet

    def get_user(self, password):
        available_user = self.check_user()

        if available_user == None:

            return 'User'

        else:
            user_info = available_user[0]
            del(user_info['_id'])

            if user_info['password'] == password:

                return user_info['name']
            else:
                return 'Password'
            

    def create_user(self, name:str, password:str, birth:str, phone:str, school:str, address:str, detail_address:str):
        unspec_wallet_info = self.get_wallet_info()
        unspec_wallet_address = unspec_wallet_info['address']
        unspec_wallet_secret = unspec_wallet_info['secret']

        user_data = UserModel().build_user_model(name, self.email, password, birth, phone, school, address, detail_address, unspec_wallet_address, unspec_wallet_secret)
        db.create_database('', '', user_data)
        db.update_database('', '', '', False, '', True)

        return True