class DeclarationModel():
    def build_declaration_model(self, user_id:str, contract_id:str, datetime:int, declaration_count:int, redeclaration:int, status:str):
        declaration_model = {
            'id' : user_id,
            'contract_id' : contract_id,
            'datetime' : datetime,
            'declaration_count' : declaration_count,
            'redeclaration' : redeclaration,
            'status' : status
        }

        return declaration_model