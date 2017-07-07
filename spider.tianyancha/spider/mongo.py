# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import pymongo
import logging

# MONGO
MONGO_URI = "localhost:27017"
mongo_client = pymongo.MongoClient(MONGO_URI)

default_db = mongo_client["tianyancha"]


class DB(object):
    def __init__(self):
        pass

    @staticmethod
    def upsert_company(company):
        logging.info("<MONGO> %s" % company)
        # default_db.company_info.update({'company_name': company['company_name']}, {'$set': company}, True, True)
