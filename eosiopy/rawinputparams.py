from eosiopy.eosioparams import EosioParams
from eosiopy.exception import ErrInputParams
from eosiopy.nodenetwork import NodeNetwork


class RawinputParams(object):

    def __init__(self, action, args, code, authorization):
        self.params = dict()
        self.raw_params = dict()
        self.raw_params["action"] = action
        self.raw_params["args"] = args
        self.raw_params["code"] = code
        self.authorization = authorization

    def get_bin(self, json_data):
        return NodeNetwork.json_to_abi(json_data=json_data)["binargs"]

    @property
    def eos_params(self):
        try:

            actor = self.authorization.split("@")[0]
            permission = self.authorization.split("@")[1]
        except:
            raise ErrInputParams()
        action = {
            "account": self.raw_params["code"],
            "authorization": [
                {
                    "actor": actor,
                    "permission": permission
                }
            ],
            "data": self.get_bin(self.raw_params),
            "name": self.raw_params["action"]
        }
        return action


if __name__ == "__main__":
    raw = RawinputParams("transfer", {
        "from": "eosio.token",
        "memo": "dd",
        "quantity": "20.0000 EOS",
        "to": "eosio"
    }, "eosio.token", "eosio.token@active")
    EosioParams(raw.eos_params)
    print(raw.eos_params)
