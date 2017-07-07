# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from scrapy.commands import ScrapyCommand
from scrapy.crawler import CrawlerRunner
from scrapy.utils.conf import arglist_to_dict
from scrapy.exceptions import UsageError

from bjda_spider.db.mongo import BjdaItemsDB
from bjda_spider.items import CompanyInfoItem


class Command(ScrapyCommand):
    requires_project = True

    def short_desc(self):
        return 'clean dirty data in bjda'

    def run(self, args, opts):
        try:
            print "===========mc_clean_dirty_data run==================="

            # skip = 0
            # limit = 10000
            # total = 236464
            # for i in range(15, total / limit + 1):
            #     skip = i * limit
            #     print "do: ", i, skip, limit
            cur = BjdaItemsDB.get_company_info_items()

            for item in cur:
                ret = CompanyInfoItem()
                ret["item_category"] = self.require_value_from_dict(item, "item_category")
                ret["item_category_num"] = self.require_value_from_dict(item, "item_category_num")
                ret["company_name"] = self.require_value_from_dict(item, "company_name")
                ret["phone"] = self.require_value_from_dict(item, "phone")
                ret["url"] = self.require_value_from_dict(item, "url")
                ret["license_number"] = self.require_value_from_dict(item, "license_number")
                ret["unified_social_credit_code"] = self.require_value_from_dict(item, "unified_social_credit_code")
                ret["organization_registration_code"] = self.require_value_from_dict(item,
                                                                                     "organization_registration_code")
                ret["registration_number"] = self.require_value_from_dict(item, "registration_number")
                ret["business_status"] = self.require_value_from_dict(item, "business_status")
                ret["business_type"] = self.require_value_from_dict(item, "business_type")
                ret["register_date"] = self.require_value_from_dict(item, "register_date")
                ret["legal_representative"] = self.require_value_from_dict(item, "legal_representative")
                ret["operating_period"] = self.require_value_from_dict(item, "operating_period")
                ret["registered_capital"] = self.require_value_from_dict(item, "registered_capital")
                ret["date_of_issue"] = self.require_value_from_dict(item, "date_of_issue")
                ret["registration_authority"] = self.require_value_from_dict(item, "registration_authority")
                ret["business_address"] = self.require_value_from_dict(item, "business_address")
                ret["business_scope"] = self.require_value_from_dict(item, "business_scope")
                BjdaItemsDB.upsert_company_info_item_clean(dict(ret))
                # print item["company_name"]
                # cur.close()

            print "===========mc_clean_dirty_data over==================="
        except Exception, e:
            print "===========mc_clean_dirty_data exception==================="
            print e.message

    def require_value_from_dict(self, dict, key):
        try:
            if isinstance(dict[key], str):
                return dict[key].strip()
            elif isinstance(dict[key], unicode):
                return dict[key].strip()
            else:
                return dict[key]
        except:
            return None
