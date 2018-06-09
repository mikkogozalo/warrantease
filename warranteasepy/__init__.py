from datetime import datetime

keys = {
    'warrantease': '5JqHARzySPxkfDoSBdiBRLKu1xgfexAFRBHozgmdmK1dFu2dt7G',
    'asus': '5HxoZKR7ffPfKABfD2LWHcxpRNseQ7Bbnk6j2B7dwrnBsBMDQpf',
    'apple': '5JWRAxUNzk2rsGyU7s9syhksN4duXv97k1ccMzC3qUcgNZn9zKZ',
    'alfred': '5HwDUSDEUeRrC7YaMLpwjHr5ExdaVFbR4Rk5NdVGJ5kk5vYGwFU',
    'olivier': '5Jg1pj5jwMNfqgS3qRcmTkM7CUKcj1Unv45XL4vJDjejcaDteri',

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
    date_of_purchase = None

    # (create)(isvalid)(addremark)(transfer)(changenick)(invalidate)(validate)(extend)

    @classmethod
    def create(cls, account, manufacturer, serial_number, length_of_warranty, coverage, region, contact_details='', remarks=''):
        w = Warranty()
        w.account = account
        w.manufacturer = manufacturer
        w.serial_number = serial_number
        w.length_of_warranty = length_of_warranty
        w.is_void = False
        w.coverage = coverage
        w.region = region
        w.contact_details = contact_details
        w.remarks = remarks