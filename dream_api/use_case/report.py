from hashlib import blake2b

from dream_api import db, blockchain
from dream_api.model.report import ReportModel

class Report():

    contract_id = '9c3c2edc'
    nft_type = '10000001'
    admin_wallet_address = 'tlink1f9wm2yfjnmxs4llcc8mw09nwtdg2urutnqjk69'
    admin_wallet_secret = '4KyYqwp2fWj47J2mUgGptdxlixhnRTIH2/X9th9N+oA='

    def __init__(self, email):
        self.email = email

    def build_index_id(self):
        hex_info = blake2b(digest_size=32, depth=255, node_depth=46, node_offset=46, inner_size=55)
        hex_info.update(b'self.email')
        index_id = hex_info.hexdigest()
        return index_id
        
    def token_index(self):
        try:
            report_info = db.read_document('Dreamer', 'REPORTS')[0]

            return report_info['token_index']

        except IndexError:

            return '00000000'


    def report_vio(self, title:str, report_type:str, content:str, datetime:int):
        report_index = self.build_index_id()
        last_token_index = self.token_index()
        token_index = '0000000' + (int(last_token_index) + 1)

        user_info = db.read_filed('Dreamer', 'USERS', 'email', self.email)[0]
        user_wallet_address = user_info['wallet']['address']
        user_name = user_info['name']

        report = ReportModel().build_report_model(report_index, token_index, report_type, self.email, datetime, 'new')
        db.create_database('Dreamer', 'REPORTS', report)
        report['content'] = content

        blockchain.mint_nft(self.contract_id, self.nft_type, self.admin_wallet_address, self.admin_wallet_secret, user_wallet_address, user_name, [report])

        return True