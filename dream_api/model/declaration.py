class DeclarationModel():
    def build_declaration_model(self, index:str, token_index:int, category:str, owner:str, datetime:int, status:str):
        declaration_model = {
            'index' : index,
            'token_index' : token_index,
            'category' : category,
            'owner' : owner,
            'datetime' : datetime,
            'status' : status
        }

        return declaration_model