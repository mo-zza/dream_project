from dream_api import db

class Login():
    def __init__(self, user_email:str):
        self.email = user_email
    
    def user_login_info(self):
        user_info_dict = db.read_database('Dreamer', 'USERS', self.email)
        user_password = user_info_dict['password']

        return user_password