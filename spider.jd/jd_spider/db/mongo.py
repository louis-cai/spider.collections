# -*- coding:utf-8 -*-
__author__ = 'zhaojm'


import pymongo


from jd_spider.settings import MONGO_URI, MONGO_PROXY_DB, MONGO_JD_DB

mongo_client = pymongo.MongoClient(MONGO_URI)
proxy_db = mongo_client[MONGO_PROXY_DB]
jd_db = mongo_client[MONGO_JD_DB]


class ProxyItemsJdDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_proxy_items():
        # print "get_proxy_items"
        return proxy_db.proxy_items_jd.find({}, {'_id': 0})


class ShellerInfoItemsDB(object):
    def __init__(self):
        pass

    @staticmethod
    def upsert_sheller_info_item(item):
        jd_db.sheller_info_items.update({
            'shop_name': item['shop_name']
        }, item, True, True)
