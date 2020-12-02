class UserModel():
    def build_user_model(self, name:str, user_email:str, password:str, birth:int, phone:int, school:str, address:str):
        user_model = {
            'user_name' : name,
            'email' : user_email,
            'password' : password,
            'birth' : birth,
            'phone' : phone,
            'school' : school,
            'address' : address,
            'status' : True,
        }

        return user_model