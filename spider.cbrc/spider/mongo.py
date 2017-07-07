# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import pymongo
import logging
import random

# MONGO
MONGO_URI = "localhost:27017"
mongo_client = pymongo.MongoClient(MONGO_URI)

cbrc_db = mongo_client["cbrc"]


class CbrcDB(object):
    def __init__(self):
        pass

    @staticmethod
    def upsert_company_1(company):
        logging.info("<MONGO> %s" % company)
        cbrc_db.company_info_1.update({u'机构编码': company[u'机构编码']}, {'$set': company}, True, True)

    @staticmethod
    def upsert_company_3(company):
        logging.info("<MONGO> %s" % company)
        cbrc_db.company_info_3.update({u'机构编码': company[u'机构编码']}, {'$set': company}, True, True)

    @staticmethod
    def upsert_company_7(company):
        logging.info("<MONGO> %s" % company)
        cbrc_db.company_info_7.update({u'机构编码': company[u'机构编码']}, {'$set': company}, True, True)

    @staticmethod
    def upsert_company_9(company):
        logging.info("<MONGO> %s" % company)
        cbrc_db.company_info_9.update({u'机构编码': company[u'机构编码']}, {'$set': company}, True, True)

    @staticmethod
    def find_flowNo(flowNo, useState):
        if useState == 1:
            if cbrc_db.company_info_1.find_one({u"流水号": "%s" % flowNo}):
                return True
            else:
                return False
        elif useState == 3:
            if cbrc_db.company_info_3.find_one({u"流水号": "%s" % flowNo}):
                return True
            else:
                return False
        elif useState == 7:
            if cbrc_db.company_info_7.find_one({u"流水号": "%s" % flowNo}):
                return True
            else:
                return False
        elif useState == 9:
            if cbrc_db.company_info_9.find_one({u"流水号": "%s" % flowNo}):
                return True
            else:
                return False
