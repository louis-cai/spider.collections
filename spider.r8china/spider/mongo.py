# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import logging

import pymongo

# MONGO
# MONGO_URI = "localhost:27017"
# mongo_client = pymongo.MongoClient(MONGO_URI)
mongo_client = pymongo.MongoClient()

r8china_db = mongo_client["r8china"]


class R8chinaDB(object):
    def __init__(self):
        pass

    @staticmethod
    def upsert_jigou(jigou):
        logging.info("<MONGO> %s" % jigou)
        r8china_db.jigou.update({'orgId': jigou['orgId']}, {'$set': jigou}, True, True)

    @staticmethod
    def upsert_jigou_2(jigou):
        logging.info("<MONGO> %s" % jigou)
        r8china_db.jigou_2.update({'orgId': jigou['orgId']}, {'$set': jigou}, True, True)

    @staticmethod
    def find_one(url):
        logging.info("<MONGO> %s" % url)
        company = r8china_db.company_info.find_one({'url': url})
        if company:
            return True
        else:
            return False
