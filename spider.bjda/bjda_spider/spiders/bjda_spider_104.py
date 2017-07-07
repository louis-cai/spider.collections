# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import scrapy

from ..items import CompanyInfoItem


class BjdaSpider(scrapy.Spider):
    name = "bjda_spider_104"

    def start_requests(self):
        req_dict_list = [

            {
                "url": "http://xzsp.bjfda.gov.cn/bfdaww/spjy/spjyAction!gzfwQueryList.dhtml",
                "totalrows": "220525", "qyfl": "1", "qyfldm": "104", "firstFlag": "clear",
                "callback": self.parse_104
            },

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
                }
                if req_dict.get("qyfl"):
                    formdata.update({
                        "qyfl": req_dict.get("qyfl"),
                        "firstFlag": req_dict.get("firstFlag"),
                        "qyfldm": req_dict.get("qyfldm"),
                    })
                print formdata
                callback = req_dict.get("callback")
                print callback
                req = scrapy.FormRequest(
                    url,
                    formdata=formdata,
                    method="GET",
                    callback=callback,
                )

                yield req

    def parse_104(self, response):
        onclicks = response.xpath("//td/img/@onclick").extract()
        for onclick in onclicks:

            xkzid = onclick.split('\'')[1]
            xksxdm = onclick.split('\'')[3]
            if "JY" == xksxdm:
                url = "/bfdaww/spjy/spjyAction!gzfwView.dhtml?spjyModel.xkzid=" + xkzid
                url = response.urljoin(url)
                req = scrapy.Request(url, callback=self.parse_company_104_jy)
                yield req
            elif "CY" == xksxdm:
                url = "/bfdaww/cyfw/cyfwAction!gzfwView.dhtml?cyfwModel.lic_id=" + xkzid
                url = response.urljoin(url)
                req = scrapy.Request(url, callback=self.parse_company_104_cy)
                yield req
            elif "LT" == xksxdm:
                url = "/bfdaww/spltqy/spltqyAction!gzfwView.dhtml?licid=" + xkzid
                url = response.urljoin(url)
                req = scrapy.Request(url, callback=self.parse_company_104_lt)
                yield req
            else:
                url = ""

    def parse_company_104_jy(self, response):
        # print response.body
        companyInfoItem = CompanyInfoItem()

        companyInfoItem['item_category'] = u"食品经营许可(含餐饮服务)"
        companyInfoItem['item_category_num'] = 104

        companyInfoItem['company_name'] = response.xpath('//table[1]/tr[1]/td[4]/text()').extract_first()
        companyInfoItem['license_number'] = response.xpath('//table[1]/tr[1]/td[2]/text()').extract_first()

        companyInfoItem['unified_social_credit_code'] = response.xpath('//table[1]/tr[2]/td[2]/text()').extract_first()

        companyInfoItem['legal_representative'] = response.xpath('//table[1]/tr[3]/td[2]/text()').extract_first()

        companyInfoItem['business_address'] = response.xpath('//table[1]/tr[4]/td[2]/text()').extract_first()

        companyInfoItem['registration_authority'] = response.xpath('//table[1]/tr[5]/td[4]/text()').extract_first()

        companyInfoItem['date_of_issue'] = response.xpath('//table[1]/tr[6]/td[4]/text()').extract_first()

        companyInfoItem['operating_period'] = response.xpath('//table[1]/tr[6]/td[2]/text()').extract_first()

        companyInfoItem['business_status'] = response.xpath('//table[1]/tr[8]/td[2]/text()').extract_first()

        companyInfoItem['business_scope'] = response.xpath('//table[1]/tr[9]/td[2]/text()').extract_first()

        # print companyInfoItem
        yield companyInfoItem

    def parse_company_104_cy(self, response):
        # print response.body
        companyInfoItem = CompanyInfoItem()

        companyInfoItem['item_category'] = u"食品经营许可(含餐饮服务)"
        companyInfoItem['item_category_num'] = 104

        companyInfoItem['company_name'] = response.xpath('//table[1]/tr[1]/td[4]/text()').extract_first()
        companyInfoItem['license_number'] = response.xpath('//table[1]/tr[1]/td[2]/text()').extract_first()

        # companyInfoItem['unified_social_credit_code'] = response.xpath('//table[1]/tr[2]/td[2]/text()').extract_first()

        companyInfoItem['legal_representative'] = response.xpath('//table[1]/tr[3]/td[2]/text()').extract_first()

        companyInfoItem['business_scope'] = response.xpath('//table[1]/tr[5]/td[2]/text()').extract_first()

        companyInfoItem['business_address'] = response.xpath('//table[1]/tr[6]/td[2]/text()').extract_first()

        # companyInfoItem['registration_authority'] = response.xpath('//table[1]/tr[5]/td[4]/text()').extract_first()

        companyInfoItem['date_of_issue'] = response.xpath('//table[1]/tr[7]/td[2]/text()').extract_first()

        companyInfoItem['operating_period'] = response.xpath('//table[1]/tr[8]/td[4]/text()').extract_first()

        companyInfoItem['business_status'] = response.xpath('//table[1]/tr[7]/td[4]/text()').extract_first()

        # print companyInfoItem
        yield companyInfoItem

    def parse_company_104_lt(self, response):
        # print response.body
        companyInfoItem = CompanyInfoItem()

        companyInfoItem['item_category'] = u"食品经营许可(含餐饮服务)"
        companyInfoItem['item_category_num'] = 104

        companyInfoItem['company_name'] = response.xpath('//table[3]/tr[1]/td[4]/text()').extract_first()
        companyInfoItem['license_number'] = response.xpath('//table[3]/tr[1]/td[2]/text()').extract_first()

        # companyInfoItem['unified_social_credit_code'] = response.xpath('//table[1]/tr[2]/td[2]/text()').extract_first()

        companyInfoItem['legal_representative'] = response.xpath('//table[3]/tr[2]/td[2]/text()').extract_first()

        companyInfoItem['business_address'] = response.xpath('//table[3]/tr[3]/td[2]/text()').extract_first()

        companyInfoItem['business_scope'] = response.xpath('//table[3]/tr[4]/td[2]/text()').extract_first()

        # companyInfoItem['registration_authority'] = response.xpath('//table[1]/tr[5]/td[4]/text()').extract_first()

        companyInfoItem['date_of_issue'] = response.xpath('//table[3]/tr[7]/td[2]/text()').extract_first()

        companyInfoItem['operating_period'] = response.xpath('//table[3]/tr[6]/td[2]/text()').extract_first()

        # companyInfoItem['business_status'] = response.xpath('//table[1]/tr[8]/td[2]/text()').extract_first()



        # print companyInfoItem
        yield companyInfoItem
