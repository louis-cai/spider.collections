# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import os
import codecs
import pymongo

mongo_client = pymongo.MongoClient()

innocom_db = mongo_client["innocom"]


def main():
    l_l = []
    for (dirpath, dirnames, filenames) in os.walk('data/beijing/'):
        year = dirpath.split('/')[-1]
        c_list = []
        for f in filenames:
            ff = "%s/%s" % (dirpath, f)
            with codecs.open(filename=ff, mode='r', encoding='utf8') as fff:
                for line in fff.readlines():
                    c_list.append(line)
        s = set(c_list)
        for item in s:
            y = {
                "date": year,
                "company_name": item
            }
            l_l.append(y)
    print l_l
    innocom_db.company_info.insert(l_l)
    pass


if __name__ == "__main__":
    main()
    pass
