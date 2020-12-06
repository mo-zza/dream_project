class ReportModel():
    def build_report_model(self, index:str, token_index:int, category:str, owner:str, datetime:int, status:str):
        report_model = {
            'index' : index,
            'token_index' : token_index,
            'category' : category,
            'owner' : owner,
            'datetime' : datetime,
            'status' : status
        }

        return report_model