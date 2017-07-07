# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import logging
import random

import pymongo

# MONGO
MONGO_URI = "localhost:27017"
mongo_client = pymongo.MongoClient(MONGO_URI)

qyxy_baic_db = mongo_client["qyxy_baic"]


# proxy_db = mongo_client['proxy']
# qianzhan_db = mongo_client['qianzhan']


class QyxybaicDB(object):
    def __init__(self):
        pass

    # @staticmethod
    # def upsert_company(company):
    #     logging.info("<MONGO> %s" % company)
    #     qyxy_baic_db.company_info.update({'reg_bus_ent_id': company['reg_bus_ent_id']}, {'$set': company}, True, True)

    # @staticmethod
    # def upsert_company_detail_level_1(company):
    #     logging.info("<MONGO> %s" % company)
    #     qyxy_baic_db.company_info_detail_level_1.update({'reg_bus_ent_id': company['reg_bus_ent_id']},
    #                                                     {'$set': company}, True,
    #                                                     True)

    @staticmethod
    def get_all():
        return qyxy_baic_db.company_info.find({}, {"_id": -1, "reg_bus_ent_id": 1}).batch_size(1)

    @staticmethod
    def get_some(num):
        count = qyxy_baic_db.company_info.find().count()
        skip = count / 5 * num
        limit = count / 5
        return qyxy_baic_db.company_info.find({}, {"_id": -1, "reg_bus_ent_id": 1}).skip(skip).limit(limit)

    @staticmethod
    def get_one(i):
        return qyxy_baic_db.company_info.find({}, {"_id": -1, "reg_bus_ent_id": 1}).skip(i).limit(1)

    @staticmethod
    def get_random_one():
        cur = qyxy_baic_db.company_info.find({}, {"_id": -1, "reg_bus_ent_id": 1})
        count = cur.count()
        i = random.randint(0, count)
        return cur[i]


class QyxybaicLevel1DB(object):
    def __init__(self):
        pass

    # @staticmethod
    # def upsert_company(company):
    #     logging.info("<MONGO> %s" % company)
    #     qyxy_baic_db.company_info.update({'reg_bus_ent_id': company['reg_bus_ent_id']}, {'$set': company}, True, True)

    @staticmethod
    def upsert_company_detail_level_1(company):
        logging.info("<MONGO> %s" % company)
        qyxy_baic_db.company_info_detail_level_1.update({'reg_bus_ent_id': company['reg_bus_ent_id']},
                                                        {'$set': company}, True,
                                                        True)

    @staticmethod
    def get_one(reg_bus_ent_id):
        return qyxy_baic_db.company_info_detail_level_1.find_one({"reg_bus_ent_id": reg_bus_ent_id})


class QyxybaicLevel2DB(object):
    def __init__(self):
        pass

    # @staticmethod
    # def upsert_company(company):
    #     logging.info("<MONGO> %s" % company)
    #     qyxy_baic_db.company_info.update({'reg_bus_ent_id': company['reg_bus_ent_id']}, {'$set': company}, True, True)

    @staticmethod
    def upsert_company_detail_level_2(company):
        logging.info("<MONGO> %s" % company)
        qyxy_baic_db.company_info_detail_level_2.update({'reg_bus_ent_id': company['reg_bus_ent_id']},
                                                        {'$set': company}, True,
                                                        True)

    @staticmethod
    def get_one(reg_bus_ent_id):
        return qyxy_baic_db.company_info_detail_level_2.find_one({"reg_bus_ent_id": reg_bus_ent_id})


class QyxybaicLevel3DB(object):
    def __init__(self):
        pass

    # @staticmethod
    # def upsert_company(company):
    #     logging.info("<MONGO> %s" % company)
    #     qyxy_baic_db.company_info.update({'reg_bus_ent_id': company['reg_bus_ent_id']}, {'$set': company}, True, True)

    @staticmethod
    def upsert_company_detail_level_3(company):
        logging.info("<MONGO> %s" % company)
        qyxy_baic_db.company_info_detail_level_3.update({'reg_bus_ent_id': company['reg_bus_ent_id']},
                                                        {'$set': company}, True,
                                                        True)

    @staticmethod
    def get_one(reg_bus_ent_id):
        return qyxy_baic_db.company_info_detail_level_3.find_one({"reg_bus_ent_id": reg_bus_ent_id})


class QyxybaicLevel4DB(object):
    def __init__(self):
        pass

    # @staticmethod
    # def upsert_company(company):
    #     logging.info("<MONGO> %s" % company)
    #     qyxy_baic_db.company_info.update({'reg_bus_ent_id': company['reg_bus_ent_id']}, {'$set': company}, True, True)

    @staticmethod
    def upsert_company_detail_level_4(company):
        logging.info("<MONGO> %s" % company)
        qyxy_baic_db.company_info_detail_level_4.update({'reg_bus_ent_id': company['reg_bus_ent_id']},
                                                        {'$set': company}, True,
                                                        True)

    @staticmethod
    def get_one(reg_bus_ent_id):
        return qyxy_baic_db.company_info_detail_level_4.find_one({"reg_bus_ent_id": reg_bus_ent_id})
