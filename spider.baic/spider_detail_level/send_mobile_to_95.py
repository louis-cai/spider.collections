# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import logging

# mongoimport -d spyj -c bjqyxxw -u supeiyunjing -p spyj2016 --file 1.json

# import logging

import pymongo
import random

# MONGO

from mongo_auth import MONGO_URI, u, p

mongo_client = pymongo.MongoClient(MONGO_URI)

db_auth = mongo_client.admin
db_auth.authenticate(u, p)
spyj_db = mongo_client["spyj"]


def upsert_to_95_bjqyxxw(reg_bus_ent_id, company_name, phone):
    logging.info("%s : %s : %s" % (reg_bus_ent_id, company_name, phone))

    spyj_db.bjqyxyw.update(
        {"reg_bus_ent_id": reg_bus_ent_id},
        {
            '$set': {
                "reg_bus_ent_id": reg_bus_ent_id, "company_name": company_name, "phone": phone
            }
        }, True, True
    )


def send_mobile_to_95(company):
    logging.info("send_mobile_to_95............")
    try:
        reg_bus_ent_id = company['reg_bus_ent_id']
        base_info = company['gsgs_info']['qynb'][-1]['qynb_detail']['base_info']
        phone = base_info[u'企业联系电话']
        company_name = base_info[u'企业名称']

        upsert_to_95_bjqyxxw(reg_bus_ent_id, company_name, phone)

        pass
    except Exception, e:
        logging.error(e.message)
        pass
    pass


def test():
    reg_bus_ent_id = "test"
    company_name = "test"
    phone = "123456789"
    upsert_to_95_bjqyxxw(reg_bus_ent_id, company_name, phone)


    # test()
