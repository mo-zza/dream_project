from hashlib import blake2b
import time
import datetime as dt
import json

from dream_api import db, blockchain
from dream_api.model.report import ReportModel

class Report():

    contract_id = '9c3c2edc'
    nft_type = '10000001'
    admin_wallet_address = 'tlink1f9wm2yfjnmxs4llcc8mw09nwtdg2urutnqjk69'
    admin_wallet_secret = '4KyYqwp2fWj47J2mUgGptdxlixhnRTIH2/X9th9N+oA='

    def build_index_id(self, owner):
        item_src = owner + str(time.time())
        item = item_src.encode()

        hex_info = blake2b(digest_size=32, depth=255, node_depth=46, node_offset=46, inner_size=55)
        hex_info.update(item)
        index_id = hex_info.hexdigest()

        return index_id
        
    def token_index(self):
        all_report_info = db.read_document('Dreamer', 'REPORTS')
        last_report = all_report_info[len(all_report_info) - 1]
        last_token_index = last_report['token_index']

        return last_token_index


    def report_vio(self, owner:str, title:str, category:str, content:str):
        report_index = self.build_index_id(owner)
        last_token_index = self.token_index()
        token_index = '000000' + str((int(last_token_index) + 1))

        user_info = db.read_filed('Dreamer', 'USERS', 'name', owner)[0]
        user_wallet_address = user_info['wallet']['address']
        datetime = dt.datetime.now()

        try:
            report_models = ReportModel(title, category, owner, datetime)
            db_model = report_models.build_report_model(report_index, token_index, 'processing')
            token_model = report_models.build_meeta_model(content)
            db.create_database('Dreamer', 'REPORTS', db_model)

            blockchain.mint_nft(self.contract_id, self.nft_type, self.admin_wallet_address, self.admin_wallet_secret, user_wallet_address, 'DIT', token_model)

            return True
        except :

            return False

    def get_report(self, report_index:str):
        report_info = db.read_filed('Dreamer', 'REPORTS', 'index', report_index)
        token_index = report_info['token_index']

        nft_info = blockchain.get_nft_info(self.contract_id, self.nft_type, token_index)
        nft_meta = nft_info['responseData']['meta']

        dict_nft_meta = json.loads(nft_meta)
        report_content = dict_nft_meta['content']

        report_info['report'] = report_content

        return report_info

    def add_count(self, report_index:str, institution:str):
        report_info = db.read_filed('Dreamer', 'REPORTS', 'index', report_index)
        old_count = report_info[institution]
        new_count = old_count + 1

        try:
            db.update_database('Dreamer', 'REPORTS', institution, old_count, institution, new_count)

            return True
        except:
            return False