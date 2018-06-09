import requests

from eosiopy.config import eosio_config


class NodeNetwork(object):
    @staticmethod
    def get_info():
        res = requests.get(eosio_config.url_port + eosio_config.get_info)
        return res.json()

    @staticmethod
    def get_block(block_num_or_id):
        res = requests.post(eosio_config.url_port + eosio_config.get_block,
                            json={"block_num_or_id": block_num_or_id})
        return res.json()

    @staticmethod
    def get_info_block():
        res = NodeNetwork.get_info()
        res.update(NodeNetwork.get_block(res["last_irreversible_block_num"]))
        return res

    @staticmethod
    def push_transaction(json_data):
        res = requests.post(eosio_config.url_port + eosio_config.push_transaction, json=json_data)
        return res.json()

    @staticmethod
    def json_to_abi(json_data):
        res = requests.post(eosio_config.url_port + eosio_config.abi_json_to_bin, json=json_data)
        print(res.text)
        return res.json()
