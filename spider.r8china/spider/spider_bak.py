# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import json
import logging
import time

import requests

from mongo import R8chinaDB


class Spider(object):
    def __init__(self):
        self._session = requests.Session()
        # JSESSIONID=BC7E0D06B1F2D37CBA466C424AD23925
        cookie_dict = {
            "JSESSIONID": "BC7E0D06B1F2D37CBA466C424AD23925"
        }
        cookies = requests.utils.cookiejar_from_dict(cookie_dict, cookiejar=None, overwrite=True)
        self._session.cookies = cookies
        pass

    def run(self):
        for i in range(1, 10):
            logging.debug("page:......%s" % i)
            self.get_search(i)
            # break

    def get_search(self, page):

        url = "http://app.r8china.cn:8080/r8/orgAPI/search.do"
        headers = {
            "Host": "app.r8china.cn:8080",
            # Content-Length	54
            "Accept": "*/*",
            "Origin": "http://app.r8china.cn:8080",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; MI 3W Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Referer": "http://app.r8china.cn:8080/r8/front/user/project.jsp?client=android&version=1.0&cuid=863360020603043&versioncode=1",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,en-US;q=0.8",
            # "Cookie":"JSESSIONID=18196AA1E9CC3010F757CB2B1A65678E",
        }

        payload = {
            "page": "%s" % page,
            "rows": "10",
            "type": "",
            "money": "",
            "period": "",
            "sortType": "",
            "keyword": "",
        }

        response = self._session.post(url=url, data=payload, headers=headers)

        jigou_list = json.loads(response.content)
        logging.debug(jigou_list)
        # exit(1)

        for jigou in jigou_list:
            orgId = jigou.get("orgId")
            logging.debug("orgId............%s" % orgId)
            org_detail = self.get_org_detail(orgId)
            recommend = self.get_recommend(orgId)
            r = {}
            r.update(jigou)
            r.update({
                "org_detail": org_detail,
                "recommend": recommend
            })
            R8chinaDB.upsert_jigou(r)
            time.sleep(1)

    def get_org_detail(self, orgId):
        url = "http://app.r8china.cn:8080/r8/orgAPI/detail.do"
        headers = {
            "Host": "app.r8china.cn:8080",
            # Content-Length	54
            "Accept": "*/*",
            "Origin": "http://app.r8china.cn:8080",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; MI 3W Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Referer": "http://app.r8china.cn:8080/r8/front/user/agency-details.jsp?id=%s&type=&money=&period=&keyword=&client=android&version=1.0&cuid=863360020603043&versioncode=1" % orgId,
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,en-US;q=0.8",
            # "Cookie":"JSESSIONID=18196AA1E9CC3010F757CB2B1A65678E",
        }
        payload = {
            "id": "%s" % orgId,
            "type": "",
            "money": "",
            "period": "",
            "idType": "",
            "insurance": "",
            "gjj": "",
            "property": "",
            "autocar": "",
            "credit": "",
            "keyword": "",
        }

        response = self._session.post(url=url, data=payload, headers=headers)

        org_detail = json.loads(response.content)
        logging.debug(org_detail)

        products_copy = []
        products = org_detail.get("products")
        for p in products:
            productId = p.get("productId")
            logging.debug("productId...........%s" % productId)
            product_detail = self.get_product_detail(productId)
            recomend = self.get_recommend(productId)
            product = {}
            product.update(p)
            product.update({
                "product_detail": product_detail,
                "recommend": recomend
            })
            products_copy.append(product)

        org_detail.update({
            "products_detail": products_copy
        })
        return org_detail

    def get_product_detail(self, productId):

        url = "http://app.r8china.cn:8080/r8/productAPI/detail.do"
        headers = {
            "Host": "app.r8china.cn:8080",
            # Content-Length	54
            "Accept": "*/*",
            "Origin": "http://app.r8china.cn:8080",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; MI 3W Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Referer": "http://app.r8china.cn:8080/r8/front/user/product-details.jsp?id=%s&client=android&version=1.0&cuid=863360020603043&versioncode=1" % productId,
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,en-US;q=0.8",
            # "Cookie":"JSESSIONID=18196AA1E9CC3010F757CB2B1A65678E",
        }
        payload = {
            "id": "%s" % productId,
        }

        response = self._session.post(url=url, data=payload, headers=headers)
        product_detail = json.loads(response.content)
        return product_detail

    def get_recommend(self, orgId):
        url = "http://app.r8china.cn:8080/r8/advisorApi/recommend.do"
        headers = {
            "Host": "app.r8china.cn:8080",
            # Content-Length	54
            "Accept": "*/*",
            "Origin": "http://app.r8china.cn:8080",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; MI 3W Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Referer": "http://app.r8china.cn:8080/r8/front/user/agency-details.jsp?id=%s&type=&money=&period=&keyword=&client=android&version=1.0&cuid=863360020603043&versioncode=1" % orgId,
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,en-US;q=0.8",
            # "Cookie":"JSESSIONID=18196AA1E9CC3010F757CB2B1A65678E",
        }
        payload = {
            "orgId": "%s" % orgId,
        }

        response = self._session.post(url=url, data=payload, headers=headers)

        recommend = json.loads(response.content)
        logging.debug(recommend)
        return recommend
