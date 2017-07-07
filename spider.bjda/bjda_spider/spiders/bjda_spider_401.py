# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import scrapy

from ..items import CompanyInfoItem


class BjdaSpider(scrapy.Spider):
    name = "bjda_spider_401"

    def start_requests(self):
        req_dict_list = [

            {
                "url": "http://xzsp.bjfda.gov.cn/bfdaww/bjpsc/bjpscAction!gzfwQueryList.dhtml",
                "totalrows": "18425", "qyfl": "4", "qyfldm": "401", "firstFlag": "clear",
                "callback": self.parse_401
            },

        ]

        for req_dict in req_dict_list:
            url = req_dict.get("url")
            totalrows = int(req_dict.get("totalrows"))
            crd = 400
            totalpages = int((totalrows + crd - 1) / crd)  # UP(totalrows/crd)
            for i in range(1, totalpages + 1):
                formdata = {
                    "ec_i": "ec",
                    "ec_p": str(i),
                    "ec_pg": str(i),
                    "ec_totalpages": str(totalpages),
                    "ec_totalrows": req_dict.get("totalrows"),
                    "ec_crd": str(crd),
                    "ec_rd": str(crd),
                    "qyfl": req_dict.get("qyfl"),
                    "firstFlag": req_dict.get("firstFlag"),
                    "qyfldm": req_dict.get("qyfldm"),
                }
                callback = req_dict.get("callback")

                req = scrapy.FormRequest(
                    url,
                    formdata=formdata,
                    method="GET",
                    callback=callback,
                )

                yield req

    def parse_401(self, response):
        onclicks = response.xpath("//td/img/@onclick").extract()
        for onclick in onclicks:
            id = onclick.split('\'')[1]
            id1 = onclick.split('\'')[3]
            url = "/bfdaww/bjpsc/bjpscAction!gzfwView.dhtml?xkzid=" + id1 + "&xkzh=" + id + "&sqlid=bjpsc.findQyjbxx&viewname=qyjbxx"

            url = response.urljoin(url)
            req = scrapy.Request(url, callback=self.parse_company_401)
            yield req

    def parse_company_401(self, response):
        # print response.body
        companyInfoItem = CompanyInfoItem()

        companyInfoItem['item_category'] = u"保健产品生产企业查询"
        companyInfoItem['item_category_num'] = 401

        companyInfoItem['company_name'] = response.xpath('//table[3]/tr[1]/td[4]/text()').extract_first()
        companyInfoItem['license_number'] = response.xpath('//table[3]/tr[1]/td[2]/text()').extract_first()

        companyInfoItem['legal_representative'] = response.xpath('//table[3]/tr[2]/td[2]/text()').extract_first()

        companyInfoItem['business_type'] = response.xpath('//table[3]/tr[2]/td[4]/text()').extract_first()

        companyInfoItem['date_of_issue'] = response.xpath('//table[3]/tr[3]/td[4]/text()').extract_first()

        companyInfoItem['operating_period'] = response.xpath('//table[3]/tr[4]/td[4]/text()').extract_first()

        companyInfoItem['business_address'] = response.xpath('//table[3]/tr[6]/td[2]/text()').extract_first()

        # companyInfoItem['unified_social_credit_code'] = response.xpath('//table[2]/tr[2]/td[2]/text()').extract_first()
        #
        # companyInfoItem['registration_authority'] = response.xpath('//table[2]/tr[6]/td[4]/text()').extract_first()

        # print companyInfoItem
        yield companyInfoItem
