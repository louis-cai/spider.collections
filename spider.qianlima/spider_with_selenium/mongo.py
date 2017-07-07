# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import pymongo
import logging

# MONGO
MONGO_URI = "localhost:27017"
mongo_client = pymongo.MongoClient(MONGO_URI)

qianlima_db = mongo_client["qianlima"]


class QianlimaDB(object):
    def __init__(self):
        pass

    @staticmethod
    def upsert_company(detail):
        logging.info("<MONGO> %s" % detail['title'])
        qianlima_db.zhongbiao_detail.update({'title': detail['title']}, {'$set': detail}, True, True)
