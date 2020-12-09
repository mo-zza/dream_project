class ReportModel():
    def __init__(self, title:str, category:str, owner:str, datetime:str):
        self.title = title
        self.category = category
        self.owner = owner
        self.datetime = datetime
        return

    def build_report_model(self, index:str, token_index:int, status:str):
        report_model = {
            'index' : index,
            'title' : self.title,
            'token_index' : token_index,
            'category' : self.category,
            'owner' : self.owner,
            'datetime' : self.datetime,
            'status' : status
        }

        return report_model

    def build_meeta_model(self, content):
        meta_model = f'{"title" : "{self.title}", "category" : "{self.category}", "owner" : "{self.owner}", "datetime" : "{self. datetime}", "content" : "{content}"}'

        return meta_model
