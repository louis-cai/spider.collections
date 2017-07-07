# -*- coding:utf-8 -*-
__author__ = 'zhaojm'


import pymongo

from qixin_spider.settings import MONGO_URI, MONGO_PROXY_DB, MONGO_JD_DB, MONGO_COMPANY_DB

mongo_client = pymongo.MongoClient(MONGO_URI)
proxy_db = mongo_client[MONGO_PROXY_DB]
jd_db = mongo_client[MONGO_JD_DB]
company_db = mongo_client[MONGO_COMPANY_DB]


class ProxyItemsQixinDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_proxy_items():
        # print "get_proxy_items"
        return proxy_db.proxy_items_qixin.find({}, {'_id': 0})


class ShellerInfoItemsDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_sheller_info_items():
        return jd_db.sheller_info_items.find()


class CompanyInfoItemsDB(object):
    def __init__(self):
        pass

    @staticmethod
    def upsert_company_info_item(item):
        company_db.company_info_items.update(
            {'company_name': item['company_name']},
            {'$set': item}, True, True)
