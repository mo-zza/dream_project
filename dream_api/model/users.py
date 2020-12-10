class UserModel():
    def build_user_model(self, user_name:str, user_email:str, password:str, birth:int, phone:int, school:str, address:str, detail_address:str, wallet_address:str, wallet_secret:str):
        user_model = {
            'email' : user_email,
            'password' : password,
            'name' : user_name,
            'school' : school,
            'phone' : phone,
            'address' : {
                'address' : address,
                'detail' : detail_address
            },
            'birth' : birth,
            'wallet' : {
                'address' : wallet_address,
                'secret' : wallet_secret
            }
        }

        return user_model