# -*- coding:utf-8 -*-
__author__ = 'zhaojm'


import pymongo

from bjda_spider.settings import MONGO_URI, MONGO_PROXY_DB, MONGO_BJDA_DB

mongo_client = pymongo.MongoClient(MONGO_URI)
proxy_db = mongo_client[MONGO_PROXY_DB]
bjda_db = mongo_client[MONGO_BJDA_DB]


class BjdaItemsDB(object):
    def __init__(self):
        pass

    @staticmethod
    def upsert_company_info_item(item):
        bjda_db.company_info_items.update({
            'company_name': item['company_name']
        }, {"$set": item}, True, True)

    @staticmethod
    def get_company_info_items():
        return bjda_db.company_info_items.find().batch_size(50)
        # return bjda_db.company_info_items.find().batch_size(50).skip(skip).limit(limit)

    @staticmethod
    def upsert_company_info_item_clean(item):
        bjda_db.company_info_items_clean.update({
            'company_name': item['company_name']
        }, {"$set": item}, True, True)


class ProxyItemsDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_proxy_items():
        return proxy_db.proxy_items_bjda.find()
