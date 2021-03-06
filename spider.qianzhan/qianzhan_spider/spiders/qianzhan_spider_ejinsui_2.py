# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import json
import random
import time
import urllib

import scrapy

from ..captcha import read_body_to_string
from ..items import CompanyInfoItem
from ..utils import get_1000_txt
from ..db.mongo import EjinsuiDB


class QianzhanSpider(scrapy.Spider):
    name = "qianzhan_spider_ejinsui_2"

    def start_requests(self):
        url = "http://qiye.qianzhan.com/usercenter/login?ReturnUrl=http%3A%2F%2Fqiye.qianzhan.com%2F"
        request = scrapy.Request(url=url, callback=self.parse_login)
        yield request

    def parse_login(self, response):
        varifyimage = response.xpath('//img[@class="code-img"]/@src').extract_first()

        url = response.urljoin(varifyimage)
        request = scrapy.Request(url=url, callback=self.parse_varifyimage)
        yield request

    def parse_varifyimage(self, response):
        varifycode = read_body_to_string(response.body)
        print "varifycode: %s" % varifycode.replace(' ', '')

        form_data = {
            "userId": "17057295997",
            "password": "123456",
            "VerifyCode": varifycode.replace(' ', ''),
            "sevenDays": "false"
        }
        url = "http://qiye.qianzhan.com/usercenter/dologin"
        request = scrapy.FormRequest(url, formdata=form_data, callback=self.parse_post_login)
        yield request

    def parse_post_login(self, response):
        # {"isSuccess":false,"sMsg":"验证码已过期，请换一张！ 登陆次数1次","dataList":null,"rowCount":0,"status":0}
        json_obj = json.loads(response.body)
        if not json_obj.get("isSuccess"):
            varifyimage = "/usercenter/varifyimage?" + str(random.random())
            url = response.urljoin(varifyimage)
            request = scrapy.Request(url=url, callback=self.parse_varifyimage)
            yield request
            return

        print "********************"
        print "login success!"
        print "********************"
        # return

        cur = EjinsuiDB.get_items()
        for item in cur:
            search_key = item['cname']
            # url = "http://qiye.qianzhan.com/orgcompany/searchlistview/qy/" + urllib.quote(
            #     search_key.encode('utf-8')) + "?o=0&area=11&areaN=%E5%8C%97%E4%BA%AC&p=1"
            # print url
            url = "http://qiye.qianzhan.com/orgcompany/searchlistview/all/" + urllib.quote(
                search_key.encode('utf-8')) + "?o=0&area=0&areaN=%E5%85%A8%E5%9B%BD&p=1"
            request = scrapy.Request(
                url,
                callback=self.parse_list
            )
            request.meta['ejinsui'] = item
            yield request
            # break
            # break

    def parse_list(self, response):

        ejinsui = response.meta['ejinsui']

        link_li_list = response.xpath('//ul[@class="list-search"]/li/p[@class="tit"]/a')
        # print "link_li_list len: ", len(link_li_list)
        for li_sel in link_li_list:
            href = li_sel.xpath('./@href').extract_first()

            url = response.urljoin(href)
            request = scrapy.Request(url, callback=self.parse_company)
            request.meta['ejinsui'] = ejinsui
            yield request
            break

            # next_page_href = response.xpath('//a[@class="next"]/@href').extract_first()
            # if next_page_href:
            #     next_page_url = response.urljoin(next_page_href)
            #     # print "next_page_url: ", next_page_url
            #     request = scrapy.Request(next_page_url, self.parse_list)
            #     yield request

    def parse_company(self, response):

        ejinsui = response.meta['ejinsui']

        company = CompanyInfoItem()

        company['ejinsui'] = ejinsui

        company['company_name'] = response.xpath('//h1[@class="ct_name"]/text()').extract_first()
        company['url'] = response.xpath('//a[@class="url"]/text()').extract_first()

        company['item_update_time'] = time.strftime('%Y-%m-%d', time.localtime(time.time()))

        ul_sel = response.xpath('//ul[@class="art-basic"]')

        company['organization_registration_code'] = ul_sel.xpath('./li[1]/span[@class="info"]/text()').extract_first()
        company['registration_number'] = ul_sel.xpath('./li[2]/span[@class="info"]/text()').extract_first()
        company['legal_representative'] = ul_sel.xpath('./li[3]/span[@class="info"]/text()').extract_first()
        company['business_status'] = ul_sel.xpath('./li[4]/span[@class="info"]/text()').extract_first()
        company['registered_capital'] = ul_sel.xpath('./li[5]/span[@class="info"]/text()').extract_first()
        company['business_type'] = ul_sel.xpath('./li[6]/span[@class="info"]/text()').extract_first()
        company['register_date'] = ul_sel.xpath('./li[7]/span[@class="info"]/text()').extract_first()
        company['operating_period'] = ul_sel.xpath('./li[8]/span[@class="info"]/text()').extract_first()
        company['business_address'] = ul_sel.xpath('./li[9]/span[@class="info"]/text()').extract_first()
        company['business_scope'] = ul_sel.xpath('./li[10]/span[@class="info"]/text()').extract_first()

        ul_sel_2 = response.xpath('//ul[@class="art-org"]')

        company['province'] = ul_sel_2.xpath('./li[2]/span[@class="info"]/text()').extract_first()
        company['registration_authority'] = ul_sel_2.xpath('./li[2]/span[@class="info"]/text()').extract_first()

        company['hdencryptCode'] = response.xpath('//input[@id="hdencryptCode"]/@value').extract_first()
        company['hdoc_area'] = response.xpath('//input[@id="hdoc_area"]/@value').extract_first()

        print "company:->", company

        url = "http://qiye.qianzhan.com/orgcompany/getcommentlist"
        form_data = {
            'orgCode': company['hdencryptCode'],
            'page': '1',
            'pagesize': '5'
        }
        request = scrapy.FormRequest(url=url, formdata=form_data, callback=self.parse_getcommentlist)
        request.meta['company'] = company
        yield request

    def parse_getcommentlist(self, response):
        company = response.meta['company']
        json_text = response.body
        json_obj = json.loads(json_text)
        print "getcommentlist:->", json_obj
        dataList = json_obj['dataList']

        company['getcommentlist'] = dataList

        url = "http://qiye.qianzhan.com/orgcompany/SearchItemCCXX"
        form_data = {
            'orgCode': company['hdencryptCode'],
            'areaCode': company['hdoc_area']
        }
        request = scrapy.FormRequest(url=url, formdata=form_data, callback=self.parse_SearchItemCCXX)
        request.meta['company'] = company
        yield request


    def parse_SearchItemCCXX(self, response):
        company = response.meta['company']
        json_text = response.body
        json_obj = json.loads(json_text)
        print "SearchItemCCXX:->", json_obj
        dataList = json_obj['dataList']

        company['SearchItemCCXX'] = dataList

        url = "http://qiye.qianzhan.com/orgcompany/searchitemdftz"
        form_data = {
            'orgName': company['company_name'],
            'page': '1',
            'pagesize': '10'
        }
        request = scrapy.FormRequest(url=url, formdata=form_data, callback=self.parse_searchitemdftz)
        request.meta['company'] = company
        yield request

    def parse_searchitemdftz(self, response):
        company = response.meta['company']
        json_text = response.body
        json_obj = json.loads(json_text)
        print "searchitemdftz:->", json_obj
        dataList = json_obj['dataList']

        company['searchitemdftz'] = dataList

        url = "http://qiye.qianzhan.com/orgcompany/searchitemnbinfo"
        form_data = {
            'orgCode': company['hdencryptCode'],
            'areaCode': company['hdoc_area']
        }
        request = scrapy.FormRequest(url=url, formdata=form_data, callback=self.parse_searchitemnbinfo)
        request.meta['company'] = company
        yield request

    def parse_searchitemnbinfo(self, response):
        company = response.meta['company']
        json_text = response.body
        json_obj = json.loads(json_text)
        print "searchitemnbinfo:->", json_obj
        dataList = json_obj['dataList']

        if isinstance(dataList, dict):
            print "++++++++++++++++  is dict +++++++++++++++"
            dataList = [dataList]

        company['searchitemnbinfo'] = dataList
        # print "searchitemnbinfo: ", dataList

        if dataList and len(dataList) > 0:
            print "+++++++++dataList is not empty+++++++++++"
            # print type(dataList)
            # print dataList
            # print dataList[0]
            url = "http://qiye.qianzhan.com/orgcompany/searchitemnb"
            form_data = {
                'orgCode': company['hdencryptCode'],
                'areaCode': company['hdoc_area'],
                'year': str(dataList[0].get('year')),
            }
            request = scrapy.FormRequest(url=url, formdata=form_data, callback=self.parse_searchitemnb)
            request.meta['company'] = company
            yield request
        else:
            print "+++++++++dataList is not empty+++++++++++"
            # yield company
            url = "http://qiye.qianzhan.com/orgcompany/searchitemsite"
            form_data = {
                'orgCode': company['hdencryptCode'],
                'page': '1',
                'pagesize': '10'
            }
            request = scrapy.FormRequest(url=url, formdata=form_data, callback=self.parse_searchitemsite)
            request.meta['company'] = company
            yield request

    def parse_searchitemnb(self, response):
        company = response.meta['company']
        json_text = response.body
        json_obj = json.loads(json_text)
        print "searchitemnb:->", json_obj
        dataList = json_obj['dataList']

        company['searchitemnb'] = dataList
        # print "searchitemnb: ", dataList

        url = "http://qiye.qianzhan.com/orgcompany/searchitemsite"
        form_data = {
            'orgCode': company['hdencryptCode'],
            'page': '1',
            'pagesize': '10'
        }
        request = scrapy.FormRequest(url=url, formdata=form_data, callback=self.parse_searchitemsite)
        request.meta['company'] = company
        yield request
        # yield company

    def parse_searchitemsite(self, response):
        company = response.meta['company']

        json_text = response.body
        json_obj = json.loads(json_text)
        print "searchitemsite:->", json_obj
        dataList = json_obj['dataList']

        company['searchitemsite'] = dataList
        # print "searchitemsite: ", dataList

        yield company
