# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import scrapy

from ..items import CompanyInfoItem


class BjdaSpider(scrapy.Spider):
    name = "bjda_spider_200"

    def start_requests(self):
        req_dict_list = [

            {
                "url": "http://xzsp.bjfda.gov.cn/bfdaww/yjjgzjxxqb/yjjgzjxxqbAction!gzfwQueryList.dhtml",
                "totalrows": "3450", "qyfl": "2", "qyfldm": "200", "firstFlag": "clear",
                "callback": self.parse_200
            }

        ]

        for req_dict in req_dict_list:
            url = req_dict.get("url")
            totalrows = int(req_dict.get("totalrows"))
            crd = 400
            totalpages = int((totalrows + crd - 1) / crd)  # UP(totalrows/crd)

            # print "url", url
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
                print formdata
                callback = req_dict.get("callback")

                req = scrapy.FormRequest(
                    url,
                    formdata=formdata,
                    method="GET",
                    callback=callback,
                )

                yield req

    def parse_200(self, response):
        onclicks = response.xpath("//td/img/@onclick").extract()
        # totalpages = response.xpath('//table[@id="ec_toolbarTable"]/tr/td[14]/nobr/text()').extract_first().split(u"共")[1].split(u"条")[0]
        for onclick in onclicks:
            url = onclick.split('\'')[1]

            url = response.urljoin(url)
            req = scrapy.Request(url, callback=self.parse_company_200)
            yield req

    def parse_company_200(self, response):
        # print response.body
        companyInfoItem = CompanyInfoItem()

        companyInfoItem['item_category'] = u"医疗机构制剂注册"
        companyInfoItem['item_category_num'] = 200

        companyInfoItem['company_name'] = response.xpath('//table[1]/tr[9]/td[2]/text()').extract_first()

        # companyInfoItem['business_address'] = response.xpath('//table[2]/tr[6]/td[4]/text()').extract_first()

        # print companyInfoItem
        yield companyInfoItem
