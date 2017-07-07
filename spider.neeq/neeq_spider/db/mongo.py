# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import pymongo

from neeq_spider.settings import MONGO_URI, MONGO_PROXY_DB, MONGO_NEEQ_DB

mongo_client = pymongo.MongoClient(MONGO_URI)
proxy_db = mongo_client[MONGO_PROXY_DB]
neeq_db = mongo_client[MONGO_NEEQ_DB]


class NeeqItemsDB(object):
    def __init__(self):
        pass

    @staticmethod
    def insert_item(item):
        # print item
        neeq_db.neeq_items.insert(item)

    @staticmethod
    def get_items():
        return neeq_db.neeq_items.find().batch_size(50)


class ProxyItemsDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_proxy_items():
        return proxy_db.proxy_items_bjda.find()
