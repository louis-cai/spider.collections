# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import scrapy

from ..items import CompanyInfoItem


class BjdaSpider(scrapy.Spider):
    name = "bjda_spider_207"

    def start_requests(self):
        req_dict_list = [

            {
                "url": "http://xzsp.bjfda.gov.cn/bfdaww/yppfqy/yppfqyAction!gzfwQueryList.dhtml",
                "totalrows": "234", "qyfl": "2", "qyfldm": "207", "firstFlag": "clear",
                "callback": self.parse_207
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

    def parse_207(self, response):
        onclicks = response.xpath("//td/img/@onclick").extract()
        for onclick in onclicks:
            zbid = onclick.split('\'')[1]
            ztid = onclick.split('\'')[3]
            url = "/bfdaww/yppfqy/yppfqyAction!gzfwView.dhtml?zbid=" + zbid + "&sqlid=yppfqy.findQyjbxx&viewname=qyjbxx&ztid=" + ztid

            url = response.urljoin(url)
            req = scrapy.Request(url, callback=self.parse_company_207)
            yield req

    def parse_company_207(self, response):
        # print response.body
        companyInfoItem = CompanyInfoItem()

        companyInfoItem['item_category'] = u"药品批发企业"
        companyInfoItem['item_category_num'] = 207

        companyInfoItem['company_name'] = response.xpath('//table[3]/tr[2]/td[2]/text()').extract_first()
        companyInfoItem['license_number'] = response.xpath('//table[3]/tr[1]/td[2]/text()').extract_first()

        companyInfoItem['business_type'] = response.xpath('//table[3]/tr[3]/td[2]/text()').extract_first()
        companyInfoItem['business_address'] = response.xpath('//table[3]/tr[2]/td[4]/text()').extract_first()

        companyInfoItem['date_of_issue'] = response.xpath('//table[3]/tr[4]/td[4]/text()').extract_first()
        companyInfoItem['operating_period'] = response.xpath('//table[3]/tr[5]/td[2]/text()').extract_first()

        # companyInfoItem['organization_registration_code'] = response.xpath('//table[2]/tr[4]/td[2]/text()').extract_first()
        # companyInfoItem['legal_representative'] = response.xpath('//table[2]/tr[5]/td[2]/text()').extract_first()
        #
        companyInfoItem['business_scope'] = response.xpath('//table[3]/tr[4]/td[2]/text()').extract_first()

        # print companyInfoItem
        yield companyInfoItem
