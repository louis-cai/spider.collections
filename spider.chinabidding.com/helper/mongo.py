# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import pymongo
import logging

# MONGO
MONGO_URI = "localhost:27017"

mongo_client = pymongo.MongoClient(MONGO_URI)

chinabidding_db = mongo_client["chinabidding"]


class ChinabiddingDB(object):
    def __init__(self):
        pass

    @staticmethod
    def upsert_result(item):
        logging.info("<MONGO> %s" % item)
        chinabidding_db.results.insert(item)

    @staticmethod
    def get_all():
        return chinabidding_db.results.find().batch_size(50)

    @staticmethod
    def upsert_company_name(company_name):
        chinabidding_db.company_name.update({'company_name': company_name}, {'$set': {"company_name": company_name}},
                                            True,
                                            True)
