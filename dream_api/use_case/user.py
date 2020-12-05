import time

from dream_api import db
from dream_api.model.users import UserModel

class Users():
    def __init__(self, user_email:str):
        self.email = user_email

    def get_wallet_info(self):
        all_wallet = db.read_filed('Dreamer', 'WALLET', 'status', False)
        unspec_wallet = all_wallet[0]

        return unspec_wallet

    def get_user(self):
        user_info = db.read_filed('Dreamer', 'USERS', 'email', self.email)
        if user_info != []:

            return user_info
        else:

            return False

    def create_user(self, name:str, password:str, birth:str, phone:str, school:str, address:str):

        if db.read_filed('Dreamer', 'USERS', 'email', self.email) == []:

            unspec_wallet_info = self.get_wallet_info()
            unspec_wallet_address = unspec_wallet_info['address']
            unspec_wallet_secret = unspec_wallet_info['secret']

            user_data = UserModel().build_user_model(name, self.email, password, birth, phone, school, address, unspec_wallet_address, unspec_wallet_secret)
            db.create_database('Dreamer', 'USERS', user_data)
            db.update_database('Dreamer', 'WALLET', 'status', False, 'status', True)

            return True

        else:

            return False