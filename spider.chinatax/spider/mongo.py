# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import pymongo
import logging
import random

# MONGO
MONGO_URI = "localhost:27017"
mongo_client = pymongo.MongoClient(MONGO_URI)

chinatax_db = mongo_client["chinatax"]


class ChinataxDB(object):
    def __init__(self):
        pass

    @staticmethod
    def upsert_company_1(company):  # 重大税收违法案件
        logging.info("<MONGO> %s" % company)
        chinatax_db.company_info_1.update({u'纳税人名称': company[u'纳税人名称']}, {'$set': company}, True, True)

    @staticmethod
    def upsert_company_2(company):  # 纳税信用A级纳税人名单公布栏
        logging.info("<MONGO> %s" % company)
        chinatax_db.company_info_2.update({'number': company['number']}, {'$set': company}, True, True)
