import arrow
from datetime import timedelta

from eosiopy.eosioparams import EosioParams
from eosiopy.nodenetwork import NodeNetwork
from eosiopy.rawinputparams import RawinputParams

import arrow

keys = {
    'warrantease': '5JqHARzySPxkfDoSBdiBRLKu1xgfexAFRBHozgmdmK1dFu2dt7G',
    'asus': '5HxoZKR7ffPfKABfD2LWHcxpRNseQ7Bbnk6j2B7dwrnBsBMDQpf',
    'apple': '5JWRAxUNzk2rsGyU7s9syhksN4duXv97k1ccMzC3qUcgNZn9zKZ',
    'alfred': '5HwDUSDEUeRrC7YaMLpwjHr5ExdaVFbR4Rk5NdVGJ5kk5vYGwFU',
    'olivier': '5Jg1pj5jwMNfqgS3qRcmTkM7CUKcj1Unv45XL4vJDjejcaDteri',
    'mikko': '5KP1sxCmruHZ8xuJP2kgkhMPWytdY6GwtoaSBarxteff51Eo7PK',
    'samsung': '5Je5TBH8o5rra4WmikspvYMHzNQe3cYmjZRM2Ca997pW48xkXor',
    'clara': '5JgnYTbiBGcarSisyoxdsSx797gXkZUcqui1hzz1sJWsMVSg5Q1',
}


class Warranty(object):
    account = None
    manufacturer = None
    serial_number = None
    date_of_purchase = None
    length_of_warranty = None
    is_void = None
    coverage = None
    region = None
    contact_details = None
    nickname = None
    remarks = None

    def to_json(self):
        dop = arrow.Arrow.fromtimestamp(self.date_of_purchase)
        expiry = (dop + timedelta(days=self.length_of_warranty)).humanize()
        return {
            'account': self.account,
            'manufacturer': self.manufacturer,
            'serial_number': self.serial_number,
            'date_of_purchase': dop.humanize(),
            'length_of_warranty': self.length_of_warranty,
            'expiry': expiry,
            'is_void': self.is_void,
            'is_valid': Warranty.is_valid(self.serial_number),
            'coverage': self.coverage,
            'region': self.region,
            'contact_details': self.contact_details,
            'nickname': self.nickname,
            'remarks': self.remarks
        }

    @classmethod
    def deserialize(cls, text):
        w = Warranty()
        ordering = ['manufacturer', 'serial_number', 'account', 'date_of_purchase', 'length_of_warranty', 'is_void', 'coverage', 'region', 'contact_details', 'nickname', 'remarks']
        values = text.split('|||')
        for k, v in zip(ordering, values):
            setattr(w, k, v)
        ints = ['serial_number', 'date_of_purchase', 'length_of_warranty']
        for k in ints:
            setattr(w, k, int(getattr(w, k)))
        w.is_void = False if w.is_void == 'false' else True
        return w

    @staticmethod
    def create(account, manufacturer, serial_number, length_of_warranty, coverage='', region='', contact_details='', remarks=''):
        raw = RawinputParams(
            "create", {
                "username": account,
                "manufacturer": manufacturer,
                "serial_number": int(serial_number),
                "length_of_warranty": int(length_of_warranty),
                "coverage": coverage,
                "region": region,
                "contact_details": contact_details,
                "remarks": remarks
            }, "warrantease", "{}@active".format(manufacturer)
        )
        eosiop_arams = EosioParams(raw.eos_params, keys[manufacturer])
        net = NodeNetwork.push_transaction(eosiop_arams.trx_json)
        return Warranty.deserialize(net['processed']['action_traces'][0]['console'])

    @staticmethod
    def change_nick(account, serial_number, nickname):
        raw = RawinputParams(
            "changenick", {
                "account": account,
                "serial_number": int(serial_number),
                "nickname": nickname
            }, "warrantease", "{}@active".format(account)
        )
        eosiop_arams = EosioParams(raw.eos_params, keys[account])
        net = NodeNetwork.push_transaction(eosiop_arams.trx_json)
        return Warranty.deserialize(net['processed']['action_traces'][0]['console'])

    @staticmethod
    def add_remark(manufacturer, serial_number, remark):
        raw = RawinputParams(
            "addremark", {
                "manufacturer": manufacturer,
                "serial_number": int(serial_number),
                "remark": remark
            }, "warrantease", "{}@active".format(manufacturer)
        )
        eosiop_arams = EosioParams(raw.eos_params, keys[manufacturer])
        net = NodeNetwork.push_transaction(eosiop_arams.trx_json)
        return Warranty.deserialize(net['processed']['action_traces'][0]['console'])

    @staticmethod
    def transfer(old_account, new_account, serial_number):
        raw = RawinputParams(
            "transfer", {
                "old_account": old_account,
                "new_account": new_account,
                "serial_number": int(serial_number)
            }, "warrantease", "{}@active".format(old_account)
        )
        eosiop_arams = EosioParams(raw.eos_params, keys[old_account])
        net = NodeNetwork.push_transaction(eosiop_arams.trx_json)
        return Warranty.deserialize(net['processed']['action_traces'][0]['console'])

    @staticmethod
    def validate(manufacturer, serial_number):
        raw = RawinputParams(
            "validate", {
                "manufacturer": manufacturer,
                "serial_number": int(serial_number)
            }, "warrantease", "{}@active".format(manufacturer)
        )
        eosiop_arams = EosioParams(raw.eos_params, keys[manufacturer])
        net = NodeNetwork.push_transaction(eosiop_arams.trx_json)
        return Warranty.deserialize(net['processed']['action_traces'][0]['console'])

    @staticmethod
    def invalidate(manufacturer, serial_number):
        raw = RawinputParams(
            "invalidate", {
                "manufacturer": manufacturer,
                "serial_number": int(serial_number)
            }, "warrantease", "{}@active".format(manufacturer)
        )
        eosiop_arams = EosioParams(raw.eos_params, keys[manufacturer])
        net = NodeNetwork.push_transaction(eosiop_arams.trx_json)
        return Warranty.deserialize(net['processed']['action_traces'][0]['console'])

    @staticmethod
    def extend(manufacturer, serial_number, days):
        raw = RawinputParams(
            "extend", {
                "manufacturer": manufacturer,
                "serial_number": int(serial_number),
                "days": int(days)
            }, "warrantease", "{}@active".format(manufacturer)
        )
        eosiop_arams = EosioParams(raw.eos_params, keys[manufacturer])
        net = NodeNetwork.push_transaction(eosiop_arams.trx_json)
        return Warranty.deserialize(net['processed']['action_traces'][0]['console'])

    @staticmethod
    def is_valid(serial_number):
        raw = RawinputParams(
            "isvalid", {
                "serial_number": int(serial_number),
            }, "warrantease", "{}@active".format('warrantease')
        )
        eosiop_arams = EosioParams(raw.eos_params, keys['warrantease'])
        net = NodeNetwork.push_transaction(eosiop_arams.trx_json)
        return True if net['processed']['action_traces'][0]['console'] == '1' else False

    @staticmethod
    def list(account):
        raw = RawinputParams(
            "list", {
                "account": account,
            }, "warrantease", "{}@active".format(account)
        )
        eosiop_arams = EosioParams(raw.eos_params, keys[account])
        net = NodeNetwork.push_transaction(eosiop_arams.trx_json)
        text = net['processed']['action_traces'][0]['console']
        items = [Warranty.deserialize(_) for _ in text.split('+++') if _]
        return items