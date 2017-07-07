# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import logging

# import time
# import urllib2

from http_client import HTTPClient

from exception import Error302, Error403, Error404, Error502, Error503, ErrorStatusCode, HttpClientError
from config import default_headers, USER_AGENTS
import random
from config import download_timeout
import requests


class SiteClient(object):
    def __init__(self, proxies):

        self._http_client = HTTPClient(proxies=proxies)
        self._user_agent = random.choice(USER_AGENTS)

        pass

    def _verify_post(self, url, data=None, json=None, times=0, headers=default_headers, timeout=download_timeout):

        headers.update({
            'User-Agent': self._user_agent,
            # "Proxy-Authorization": self.get_authHeader()
        })

        try:
            response = self._http_client.post(url=url, data=data, json=json, headers=headers, timeout=timeout)
            if response.status_code == 200:
                # logging.debug(response.headers)
                pass
            elif response.status_code == 302:
                location = response.headers['Location']
                logging.debug("location: %s" % location)
                raise Error302()
            elif response.status_code == 403:
                raise Error403()
            elif response.status_code == 404:
                raise Error404()
            elif response.status_code == 502:
                raise Error502()
            elif response.status_code == 503:
                raise Error503()
            else:
                raise ErrorStatusCode(response.status_code)
            return response
        except Error403, err:
            raise err
        except HttpClientError, err:
            times += 1
            if times < 2:
                return self._verify_post(url, data=data, json=json, times=times, headers=headers, timeout=timeout)
            else:
                raise err

    def _verify_get(self, url, times=0, headers=default_headers, refresh_ip=False, timeout=download_timeout):
        headers.update({
            'User-Agent': self._user_agent,
            # "Proxy-Authorization": self.get_authHeader(refresh_ip)
        })
        try:
            response = self._http_client.get(url, headers=headers, timeout=timeout)
            if response.status_code == 200:
                # logging.debug(response.headers)
                pass
            elif response.status_code == 302:
                location = response.headers['Location']
                logging.debug("location: %s" % location)
                raise Error302()
            elif response.status_code == 403:
                raise Error403()
            elif response.status_code == 404:
                raise Error404()
            elif response.status_code == 502:
                raise Error502()
            else:
                raise ErrorStatusCode(response.status_code)
            return response
        except Error403, err:
            raise err
        except HttpClientError, err:
            times += 1
            if times < 2:
                return self._verify_get(url, times=times, headers=headers, refresh_ip=refresh_ip, timeout=timeout)
            else:
                raise err

    def get_search(self, url):
        # response = self._verify_get(url)
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.6,en-US;q=0.4,en;q=0.2',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            # 'Cookie':'LastCity=%e5%8c%97%e4%ba%ac; LastCity%5Fid=530; JSSearchModel=0; dywez=95841923.1479792930.7.4.dywecsr=sou.zhaopin.com|dyweccn=(referral)|dywecmd=referral|dywectr=undefined|dywecct=/jobs/companysearch.ashx; LastSearchHistory=%7b%22Id%22%3a%22d0666d66-6af1-4382-92b2-9495130e1e3e%22%2c%22Name%22%3a%22%e5%8c%97%e4%ba%ac%22%2c%22SearchUrl%22%3a%22http%3a%2f%2fsou.zhaopin.com%2fjobs%2fsearchresult.ashx%3fsm%3d0%26p%3d1%22%2c%22SaveTime%22%3a%22%5c%2fDate(1479794038936%2b0800)%5c%2f%22%7d; _qzja=1.885675296.1479794024618.1479794024618.1479794024619.1479794049541.1479794183278.0.0.0.3.1; _qzjc=1; _qzjto=3.1.0; _jzqx=1.1479198437.1479796291.4.jzqsr=baidu%2Ecom|jzqct=/.jzqsr=company%2Ezhaopin%2Ecom|jzqct=/cc668471724%2Ehtm; _jzqckmp=1; JSSearchCompanyID=cc668471724; _jzqa=1.2350289612473381000.1479198437.1479792952.1479796291.7; _jzqc=1; _jzqb=1.2.10.1479796291.1; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1479198436,1479450538; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1479797791; dywea=95841923.2267255849444585000.1477666294.1479786879.1479792930.7; dywec=95841923; dyweb=95841923.36.10.1479792930; __utmt=1; __utma=269921210.150849714.1477666295.1479792930.1479797791.8; __utmb=269921210.1.10.1479797791; __utmc=269921210; __utmz=269921210.1479792930.7.4.utmcsr=sou.zhaopin.com|utmccn=(referral)|utmcmd=referral|utmcct=/jobs/companysearch.ashx; urlfrom=121126445; urlfrom2=121126445; adfcid=none; adfcid2=none; adfbid=0; adfbid2=0',
            'Host': 'bj.58.com',
            'Pragma': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
        }
        # response = self._verify_get(url, headers=headers)
        response = requests.get(url, headers=headers)
        return response

    def get_job(self, url):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.6,en-US;q=0.4,en;q=0.2',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            # 'Cookie':'LastCity=%e5%8c%97%e4%ba%ac; LastCity%5Fid=530; JSSearchModel=0; dywez=95841923.1479792930.7.4.dywecsr=sou.zhaopin.com|dyweccn=(referral)|dywecmd=referral|dywectr=undefined|dywecct=/jobs/companysearch.ashx; LastSearchHistory=%7b%22Id%22%3a%22d0666d66-6af1-4382-92b2-9495130e1e3e%22%2c%22Name%22%3a%22%e5%8c%97%e4%ba%ac%22%2c%22SearchUrl%22%3a%22http%3a%2f%2fsou.zhaopin.com%2fjobs%2fsearchresult.ashx%3fsm%3d0%26p%3d1%22%2c%22SaveTime%22%3a%22%5c%2fDate(1479794038936%2b0800)%5c%2f%22%7d; _qzja=1.885675296.1479794024618.1479794024618.1479794024619.1479794049541.1479794183278.0.0.0.3.1; _qzjc=1; _qzjto=3.1.0; _jzqx=1.1479198437.1479796291.4.jzqsr=baidu%2Ecom|jzqct=/.jzqsr=company%2Ezhaopin%2Ecom|jzqct=/cc668471724%2Ehtm; _jzqckmp=1; JSSearchCompanyID=cc668471724; _jzqa=1.2350289612473381000.1479198437.1479792952.1479796291.7; _jzqc=1; _jzqb=1.2.10.1479796291.1; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1479198436,1479450538; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1479797791; dywea=95841923.2267255849444585000.1477666294.1479786879.1479792930.7; dywec=95841923; dyweb=95841923.36.10.1479792930; __utmt=1; __utma=269921210.150849714.1477666295.1479792930.1479797791.8; __utmb=269921210.1.10.1479797791; __utmc=269921210; __utmz=269921210.1479792930.7.4.utmcsr=sou.zhaopin.com|utmccn=(referral)|utmcmd=referral|utmcct=/jobs/companysearch.ashx; urlfrom=121126445; urlfrom2=121126445; adfcid=none; adfcid2=none; adfbid=0; adfbid2=0',
            'Host': 'bj.58.com',
            'Pragma': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
        }
        # response = self._verify_get(url, headers=headers)
        response = requests.get(url, headers=headers)
        return response

        # def get_company(self, url):
        #
        #     headers = {
        #         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        #         'Accept-Encoding': 'gzip, deflate, sdch',
        #         'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.6,en-US;q=0.4,en;q=0.2',
        #         'Cache-Control': 'no-cache',
        #         'Connection': 'keep-alive',
        #         # 'Cookie':'LastCity=%e5%8c%97%e4%ba%ac; LastCity%5Fid=530; JSSearchModel=0; dywez=95841923.1479792930.7.4.dywecsr=sou.zhaopin.com|dyweccn=(referral)|dywecmd=referral|dywectr=undefined|dywecct=/jobs/companysearch.ashx; LastSearchHistory=%7b%22Id%22%3a%22d0666d66-6af1-4382-92b2-9495130e1e3e%22%2c%22Name%22%3a%22%e5%8c%97%e4%ba%ac%22%2c%22SearchUrl%22%3a%22http%3a%2f%2fsou.zhaopin.com%2fjobs%2fsearchresult.ashx%3fsm%3d0%26p%3d1%22%2c%22SaveTime%22%3a%22%5c%2fDate(1479794038936%2b0800)%5c%2f%22%7d; _qzja=1.885675296.1479794024618.1479794024618.1479794024619.1479794049541.1479794183278.0.0.0.3.1; _qzjc=1; _qzjto=3.1.0; _jzqx=1.1479198437.1479796291.4.jzqsr=baidu%2Ecom|jzqct=/.jzqsr=company%2Ezhaopin%2Ecom|jzqct=/cc668471724%2Ehtm; _jzqckmp=1; JSSearchCompanyID=cc668471724; _jzqa=1.2350289612473381000.1479198437.1479792952.1479796291.7; _jzqc=1; _jzqb=1.2.10.1479796291.1; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1479198436,1479450538; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1479797791; dywea=95841923.2267255849444585000.1477666294.1479786879.1479792930.7; dywec=95841923; dyweb=95841923.36.10.1479792930; __utmt=1; __utma=269921210.150849714.1477666295.1479792930.1479797791.8; __utmb=269921210.1.10.1479797791; __utmc=269921210; __utmz=269921210.1479792930.7.4.utmcsr=sou.zhaopin.com|utmccn=(referral)|utmcmd=referral|utmcct=/jobs/companysearch.ashx; urlfrom=121126445; urlfrom2=121126445; adfcid=none; adfcid2=none; adfbid=0; adfbid2=0',
        #         'Host': 'qy.58.com',
        #         'Pragma': 'no-cache',
        #         'Upgrade-Insecure-Requests': '1',
        #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
        #     }
        #     response = self._verify_get(url, headers=headers)
        #     return response
