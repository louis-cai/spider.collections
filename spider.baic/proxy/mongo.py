# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import pymongo
import logging

# MONGO
MONGO_URI = "localhost:27017"
mongo_client = pymongo.MongoClient(MONGO_URI)
proxy_db = mongo_client['proxy']


class ProxyItemsDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_proxy_items():
        return proxy_db.proxy_items_all.find({"get": True, "post": True}, {'_id': 0}).batch_size(10)

    @staticmethod
    def upsert_proxy_item(item):
        proxy_db.proxy_items_all.update({"ip": item['ip'], "port": item['port']}, item, True, True)

    @staticmethod
    def remove_proxy_item(item):
        proxy_db.proxy_items_all.remove({"ip": item['ip'], "port": item['port']})


class AlivebaicDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_proxy_items():
        return proxy_db.proxy_items_baic.find({}, {'_id': 0}).batch_size(10)

    @staticmethod
    def upsert_proxy_item(item):
        proxy_db.proxy_items_baic.update({"ip": item['ip'], "port": item['port']}, item, True, True)

    @staticmethod
    def remove_proxy_item(item):
        proxy_db.proxy_items_baic.remove({"ip": item['ip'], "port": item['port']})
