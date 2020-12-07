from dream_api import db

class Modify():
    def __init__(self, report_index:str, report_status:str):
        self.index = report_index
        self.status = report_status

    def report_modify(self):
        try:
            db.update_database('Dreamer', 'REPORTS', 'index', self.index, 'status', self.status)

            return True

        except:
            
            return False
            
