# -*- coding:utf-8 -*-
__author__ = 'zhaojm'
import logging

import pymongo

from log import init_logging

mongo_client = pymongo.MongoClient()

r8china_db = mongo_client["r8china"]

jigou_2_collection = r8china_db.jigou_2

cur = jigou_2_collection.find()


def main():
    jigou_list = []
    for jigou in cur:
        jigou_copy = {}

        name = jigou.get("name")
        jigou_copy.update({
            "orgname": name,
        })

        listwitharg = jigou.get('listwitharg')
        i = 0
        for contact in listwitharg:
            name = contact.get("name")
            contactName = contact.get("contactName")
            contactPhone = contact.get("contactPhone")
            jigou_copy.update({
                "contact_%s_name" % i: name,
                "contact_%s_contactName" % i: contactName,
                "contact_%s_contactPhone" % i: contactPhone
            })
            i += 1

        products_detail = jigou.get("org_detail").get("products_detail")
        i = 0
        for product in products_detail:
            productname = product.get("productname")
            productType = product.get("productType")
            rate = product.get("rate")
            lowerNum = product.get("lowerNum")
            upperNum = product.get("upperNum")
            lowerPeriod = product.get("lowerPeriod")
            upperPeriod = product.get("upperPeriod")
            loanDate = product.get("loanDate")

            jigou_copy.update({
                "product_%s_productname" % i: productname,
                "product_%s_productType" % i: productType,
                "product_%s_rate" % i: rate,
                "product_%s_lowerNum" % i: lowerNum,
                "product_%s_upperNum" % i: upperNum,
                "product_%s_lowerPeriod" % i: lowerPeriod,
                "product_%s_upperPeriod" % i: upperPeriod,
                "product_%s_loanDate" % i: loanDate
            })
            i += 1
        jigou_list.append(jigou_copy)
        # logging.info(jigou_copy)
    # logging.info(jigou_list)
    # r8china_db.export_jigou_2_csv.insert(jigou_list)

    json_list_to_csv(jigou_list)


def json_list_to_csv(json_list):
    keys = []
    for obj in json_list:
        keys.extend(obj.keys())

    keys = set(keys)
    keys = list(keys)
    keys.sort()

    lines = []
    lines.append(','.join(keys) + ',')
    for obj in json_list:
        line = ''
        for key in keys:
            line += "%s," % obj.get(key, '')
        lines.append(line)

    logging.info(lines)

    txt = '\n'.join(lines)

    logging.info(txt)
    import codecs
    f = codecs.open(filename="1.csv", encoding="utf8", mode="w")
    f.write(txt)
    f.close()


if __name__ == "__main__":
    init_logging()
    main()
