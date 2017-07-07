# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import scrapy

from ..items import CompanyInfoItem


class BjdaSpider(scrapy.Spider):
    name = "bjda_spider_103"

    def start_requests(self):
        req_dict_list = [
            {
                "url": "http://xzsp.bjfda.gov.cn/bfdaww/spscqy/spscqyAction!gzfwQueryList.dhtml",
                "totalrows": "1652",
                "callback": self.parse
            }
        ]

        for req_dict in req_dict_list:
            url = req_dict.get("url")
            totalrows = int(req_dict.get("totalrows"))
            crd = 200
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

    def parse(self, response):
        onclicks = response.xpath("//td/img/@onclick").extract()
        for onclick in onclicks:
            xkzid = onclick.split('\'')[3]
            url = "/bfdaww/spscqy/spscqyAction!gzfwView.dhtml?spscqyModel.chr_id=" + xkzid + "&viewname=view&type=jbxx"

            url = response.urljoin(url)
            print url
            req = scrapy.Request(url, callback=self.parse_company_103)
            yield req

    def parse_company_103(self, response):
        # print response.body
        companyInfoItem = CompanyInfoItem()

        companyInfoItem['item_category'] = u"食品生产许可"
        companyInfoItem['item_category_num'] = 103

        companyInfoItem['company_name'] = response.xpath('//table[3]/tr[1]/td[2]/text()').extract_first()
        companyInfoItem['license_number'] = response.xpath('//table[3]/tr[1]/td[4]/text()').extract_first()

        companyInfoItem['unified_social_credit_code'] = response.xpath('//table[3]/tr[2]/td[2]/text()').extract_first()

        companyInfoItem['legal_representative'] = response.xpath('//table[3]/tr[3]/td[2]/text()').extract_first()

        companyInfoItem['business_address'] = response.xpath('//table[3]/tr[5]/td[2]/text()').extract_first()

        companyInfoItem['registration_authority'] = response.xpath('//table[3]/tr[6]/td[4]/text()').extract_first()

        companyInfoItem['operating_period'] = response.xpath('//table[3]/tr[7]/td[2]/text()').extract_first()

        # print companyInfoItem
        yield companyInfoItem
