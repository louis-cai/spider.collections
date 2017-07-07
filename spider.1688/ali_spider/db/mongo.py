# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import pymongo

from ali_spider.settings import MONGO_URI, MONGO_PROXY_DB, MONGO_ALI_DB

mongo_client = pymongo.MongoClient(MONGO_URI)
proxy_db = mongo_client[MONGO_PROXY_DB]
ali_db = mongo_client[MONGO_ALI_DB]


class ProxyItemsAliDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_proxy_items():
        # print "get_proxy_items"
        return proxy_db.proxy_items_ali.find({}, {'_id': 0})


class ShellerInfoItemsDB(object):
    def __init__(self):
        pass

    @staticmethod
    def upsert_sheller_info_item(item):
        ali_db.sheller_info_items.update({
            'shop_name': item['shop_name']
        }, item, True, True)
