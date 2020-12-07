import requests
import random
import string
import time
import hmac
import hashlib
import base64


class BlockchainRequest():
    def __init__(self, api_key, secret_key, base_url):
        self.__key = api_key
        self.__secret = secret_key
        self.base_url = base_url

    def create_nonce(self):
        nonce = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(8))

        return nonce

    def get_server_time(self):
        end_point = '/v1/time'

        headers = {
            'service-api-key' : self.__key,
        }

        res = requests.get(self.base_url + end_point, headers=headers)

        return res.json()['responseTime']

    def hashing(self, data):
        sha_hex = hmac.new(str.encode(self.__secret), str.encode(data), digestmod=hashlib.sha512)
        signature = base64.b64encode(sha_hex.digest())

        return signature

    def create_path_only_signature(self, method, end_point):
        nonce = self.create_nonce()
        timestamp = self.get_server_time()

        data = nonce+str(timestamp)+method+end_point
        signature = self.hashing(data)

        return signature, nonce, timestamp

    def build_path_only_headers(self, method, end_point):
        signature, nonce, timestamp = self.create_path_only_signature(method, end_point)

        headers = {
            'service-api-key' : self.__key,
            'signature' : signature,
            'timestamp' : str(timestamp),
            'nonce' : nonce
        }

        return headers

    def create_request_body_signature(self, method, end_point, body):
        nonce=self.create_nonce()
        timestamp=self.get_server_time()

        data = nonce+str(timestamp)+method+end_point+body
        signature=self.hashing(data)

        return signature, nonce, timestamp

    def build_request_body_headers(self, method, end_point, body):
        signature, nonce, timestamp = self.create_request_body_signature(method, end_point, body)

        headers = {
            'service-api-key' : self.__key,
            'signature' : signature,
            'timestamp' : str(timestamp),
            'nonce' : nonce,
            'Content-type' : 'application/json'
        }

        return headers


class LineBlockchain(BlockchainRequest):
    def __init__(self, base_url='https://test-api.blockchain.line.me', api_key='2b885173-b3ba-4f67-8a2d-0dda9a0ab99b', secret_key='91ba4ec6-5a00-4d00-889d-5cb46d073be7'):
        super().__init__(api_key, secret_key, base_url)

    def get_service_information(self, serviceId):
        end_point = f'/v1/services/{serviceId}'
        # end_point = '/v1/wallets'

        header = self.build_path_only_headers('GET', end_point)

        res = requests.get(self.base_url + end_point, headers=header)
        return res.json()

    def get_all_wallet(self):
        end_point = '/v1/wallets'

        header = self.build_path_only_headers('GET', end_point)

        res = requests.get(self.base_url + end_point, headers=header)
        return res.json()


    def get_all_service_token(self):
        end_point = '/v1/service-tokens'

        header = self.build_path_only_headers('GET', end_point)

        res = requests.get(self.base_url + end_point, headers=header)

        return res.json()

    def create_service_token(self, contractId, ownerAddress, ownerSecret, amount):
        end_point = f'/v1/service-tokens/{contractId}/mint'

        request_body = {
            'ownerAddress' : ownerAddress,
            'ownerSecret': ownerSecret,
            'amount': amount,
            'Content-Type' : 'application/json'
        }

        uri = f'?amount={amount}&ownerAddress={ownerAddress}&ownerSecret={ownerSecret}'

        header = self.build_request_body_headers('POST', end_point, uri)

        res = requests.post(self.base_url + end_point, headers=header, json=request_body)

        return res.json()

    def get_all_ft_contract_info(self, contractId):
        end_point = f'/v1/item-tokens/{contractId}'

        header = self.build_path_only_headers('GET', end_point)

        res = requests.get(self.base_url + end_point, headers=header)

        return res.json()

    def get_all_nft_contract_info(self, contractId):
        end_point = f'/v1/item-tokens/{contractId}/non-fungibles'

        header = self.build_path_only_headers('GET', end_point)

        res = requests.get(self.base_url + end_point, headers=header)

        return res.json()

    def create_nft(self, contractId, ownerAddress, ownerSecret, name, meta):
        end_point = f'/v1/item-tokens/{contractId}/non-fungibles'

        request_body = {
            'ownerAddress' : ownerAddress,
            'ownerSecret': ownerSecret,
            'name' : name,
            'meta' : meta
        }

        uri = f'?name={name}&meta={meta}&ownerAddress={ownerAddress}&ownerSecret={ownerSecret}'

        header = self.build_request_body_headers('POST', end_point, uri)

        res = requests.post(self.base_url + end_point, headers=header, json=request_body)

        return res.json()

    def mint_nft(self, contractId, tokenType, ownerAddress, ownerSecret, toAddress, name, meta):
        end_point = f'/v1/item-tokens/{contractId}/non-fungibles/{tokenType}/mint'

        request_body = {
            'name': name,
            'meta': meta,
            'ownerAddress': ownerAddress,
            'ownerSecret': ownerSecret,
            'toAddress': toAddress,
        }

        uri = f'?meta={meta}&name={name}&ownerAddress={ownerAddress}&ownerSecret={ownerSecret}&toAddress={toAddress}'
        
        header = self.build_request_body_headers('POST', end_point, uri)

        res = requests.post(self.base_url + end_point, headers=header, json=request_body)
        
        return res.json()

    def get_nft_info(self, contractId, tokenType, tokenIndex):
        end_point = f'/v1/item-tokens/{contractId}/non-fungibles/{tokenType}/{tokenIndex}'

        header = self.build_path_only_headers('GET', end_point)

        res = requests.get(self.base_url + end_point, headers=header)

        return res.json()