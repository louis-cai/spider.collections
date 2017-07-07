# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import logging

import pymongo

from log import init_logging

# MONGO
MONGO_URI = "localhost:27017"
mongo_client = pymongo.MongoClient(MONGO_URI)

qyxy_baic_db = mongo_client["qyxy_baic"]

cur = qyxy_baic_db.company_info_detail_level_1.find()

init_logging('1.log', '2.log')

if __name__ == "__main__":
    try:
        for item in cur:
            try:
                reg_bus_ent_id = item['reg_bus_ent_id']
                base_info = item['gsgs_info']['qynb'][-1]['qynb_detail']['base_info']
                phone = base_info[u'企业联系电话']
                company_name = base_info[u'企业名称']
                logging.info("%s : %s : %s" % (reg_bus_ent_id, company_name, phone))
                qyxy_baic_db.export_from_level_1.update(
                    {"reg_bus_ent_id": reg_bus_ent_id},
                    {
                        '$set': {
                            "reg_bus_ent_id": reg_bus_ent_id, "company_name": company_name, "phone": phone
                        }
                    }, True, True
                )
                pass
            except Exception, e:
                logging.error(e.message)
                pass
    except Exception, e:
        logging.exception(e)
        pass
