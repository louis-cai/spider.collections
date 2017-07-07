# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import pymongo
import logging

# MONGO
MONGO_URI = "localhost:27017"
mongo_client = pymongo.MongoClient(MONGO_URI)

# qyxy_baic_db = mongo_client["qyxy_baic"]
proxy_db = mongo_client['proxy']
qianzhan_db = mongo_client['qianzhan']
baidubaike_db = mongo_client['baidubaike']


# class QyxybaicDB(object):
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def upsert_company(company):
#         logging.info("<MONGO> %s" % company)
#         qyxy_baic_db.company_info.update({'reg_bus_ent_id': company['reg_bus_ent_id']}, {'$set': company}, True, True)
#
#
# class ProxyDB(object):
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def get_all():
#         return proxy_db.proxy_items_baic.find().batch_size(1)
#
#     @staticmethod
#     def remove_proxy(proxy_ip, proxy_port):
#         proxy_db.proxy_items_baic.remove({"ip": proxy_ip, "port": proxy_port})


class QianzhanDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_all_count():
        return qianzhan_db.company_info_items_base.find({"province": "北京"}).count()

    @staticmethod
    def get_one(i):
        return qianzhan_db.company_info_items_base.find({"province": "北京"})[i]

    @staticmethod
    def get_all():
        return qianzhan_db.company_info_items_base.find().batch_size(1)

    @staticmethod
    def upsert_company(item):
        logging.info("<MONGO> %s" % item)
        qianzhan_db.company_info_items_base.update({'company_name': item['company_name']}, {'$set': item}, True, True)

    @staticmethod
    def is_had(company_name):
        cur = qianzhan_db.company_info_items_base.find_one({"company_name": company_name})
        # logging.debug("cur:%s" % cur)
        if cur:
            return True
        else:
            return False


class BaidubaikeDB(object):
    def __init__(self):
        pass

    @staticmethod
    def upsert_compnay(item):
        logging.info("<MONGO> %s" % item)
        baidubaike_db.company_info.update({'company_name': item['company_name']}, {'$set': item}, True, True)
