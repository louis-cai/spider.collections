# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from neeq_spider.db.mongo import NeeqItemsDB


def main():
    cur = NeeqItemsDB.get_items()

    for obj in cur:
        baseinfo = obj.get("baseinfo")
        company_name = baseinfo.get("name")

    pass


if __name__ == "__main__":
    main()
    pass
