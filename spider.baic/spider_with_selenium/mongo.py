# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import pymongo
import logging

# MONGO
MONGO_URI = "localhost:27017"
mongo_client = pymongo.MongoClient(MONGO_URI)

qyxy_baic_db = mongo_client["qyxy_baic"]
proxy_db = mongo_client['proxy']


class QyxybaicDB(object):
    def __init__(self):
        pass

    @staticmethod
    def upsert_company(company):
        logging.info("<MONGO> %s" % company)
        qyxy_baic_db.company_info.update({'reg_bus_ent_id': company['reg_bus_ent_id']}, {'$set': company}, True, True)


class ProxyDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_all():
        return proxy_db.proxy_items_baic.find().batch_size(10)

    @staticmethod
    def remove_proxy(proxy_ip, proxy_port):
        proxy_db.proxy_items_baic.remove({"ip": proxy_ip, "port": proxy_port})
