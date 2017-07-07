# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from utils import get_gb2312_txt
import time
import urllib
import requests
import json

from mongo import Company


class Spider(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'android:HONOR H30-L01;4.4.2;2.2.0',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'app1.entplus.cn:8082',
        }

    def start(self):
        txt = get_gb2312_txt()
        for i in range(len(txt)):
            for j in range(len(txt)):
                search_key = txt[i] + txt[j]
                print "gb2312:-> " + time.strftime('%Y-%m-%d', time.localtime(time.time())) + str(i) + str(j) + str(
                    len(txt)) + str(search_key)
                try:
                    self.request_list(search_key, 1)
                except Exception, e:
                    print "request_list Exception:-> " + "search_key: " + str(search_key) + ", page: 1, e: " + e.message
                    pass
                    # break
                    # break

    def request_list(self, search_key, page):
        print "request_list:-> search_key: " + str(search_key) + ", page: " + str(page)
        url = "http://app1.entplus.cn:8082/entplus//company/fQyEnterprisebaseinfoListArea"
        payload = {
            'os': 'android',
            'source_id': 'Yek_test',
            'imei': '864502020269817',
            'keyword': search_key,
            'app_key': 123456,
            'ver': '1.0',
            'type': 1,
            'areaId': '',
            'os_version': '4.4.2',
            'rows': 20,
            'mobileModel': 'HONOR+H30-L01',
            'appVersion': '2.2.0',
            'page': page,
            'userId': 'ff808081555c04fe0155d8b8dd221d7a',
            'appChannel': 'offical',
            # 'time_stamp': '20160711145140'
            'time_stamp': time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        }

        response = requests.post(url=url, data=payload, headers=self.headers)
        txt = response.text
        txt_json = json.loads(txt)
        if txt_json.get('respCode') == u'0':
            data = txt_json.get('data')

            company_list = data.get("list")
            self.parse_list(company_list)

            totalPages = data.get('totalPages')
            print 'totalPages: ' + str(totalPages)
            if page < int(totalPages):
                try:
                    self.request_list(search_key, page + 1)
                except Exception, e:
                    print "request_list Exception:-> " + "search_key: " + str(search_key) + ", page: 1, e: " + e.message
                    pass
            else:
                print 'over:-> ' + \
                      time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + \
                      ', search_key: ' + str(search_key) + \
                      ', totalPages: ' + str(totalPages)
        else:
            print "respCode: " + txt_json.get('respCode') + ", respDesc: " + txt_json.get("respDesc")

    def parse_list(self, company_list):
        for company in company_list:
            lcid = company.get('lcid')
            try:
                self.request_company(lcid)
            except Exception, e:
                print "request_company Exception:-> " + "lcid: " + lcid + ", e: " + e.message
        pass

    def request_company(self, lcid):
        url = "http://app1.entplus.cn:8082/entplus//company/newfQyEnterprisebaseinfo?mobileModel=HONOR+H30-L01&lcid=" + lcid + "&os=android&appVersion=2.2.0&source_id=Yek_test&imei=864502020269817&userId=ff808081555c04fe0155d8b8dd221d7a&app_key=123456&appChannel=offical&ver=1.0&type=1&time_stamp=" + time.strftime(
            '%Y%m%d%H%M%S', time.localtime(time.time())) + "&os_version=4.4.2"
        # payload = {
        #     'os': 'android',
        #     'source_id': 'Yek_test',
        #     'imei': '864502020269817',
        #     'lcid': lcid,
        #     'app_key': 123456,
        #     'ver': '1.0',
        #     'type': 1,
        #     'areaId': '',
        #     'os_version': '4.4.2',
        #     'mobileModel': 'HONOR+H30-L01',
        #     'appVersion': '2.2.0',
        #     'userId': 'ff808081555c04fe0155d8b8dd221d7a',
        #     'appChannel': 'offical',
        #     # 'time_stamp': '20160711145140'
        #     'time_stamp': time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        # }

        response = requests.get(url=url, headers=self.headers)
        txt = response.text
        txt_json = json.loads(txt)
        if txt_json.get('respCode') == u'0':
            data = txt_json.get('data')
            self.parse_company(data)
        else:
            print "respCode: " + txt_json.get('respCode') + ", respDesc: " + txt_json.get("respDesc")
        pass

    def parse_company(self, company):
        Company.upsert(company)
