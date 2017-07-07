# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import logging
from bs4 import BeautifulSoup
from exception import Error302, Error403, Error404, Error502, Error503, ErrorStatusCode, HttpClientError, \
    MoreCheckverifyCodeTimesError, NeedrefreshProxyError, UnknownTitle
from mongo import BjsatDB, QianzhanDB
from mredis import RedisClient
from site_client import SiteClient
# from captcha import read_body_to_string
from utils import get_1000_txt
from config import skip_num
from get_proxy import GetProxy


class Spider(object):
    # 税务登记及一般纳税人资格信息
    def __init__(self):
        self._txt = get_1000_txt()
        self._getProxy = GetProxy()
        self._proxy_ip = None
        self._proxy_port = None
        pass

    def run(self, type):
        logging.info("+++++++++++++run++++++++++++++++")
        try:
            if type == 1:
                self._run()
            elif type == 2:
                self._run_2()
            else:
                raise Exception("error run type")
            logging.info("++++++++++++++success finish!!!++++++++")
        except Exception, e:
            logging.exception(e.message)
            # self.run()
            pass

    def _run(self):
        for i in range(0, len(self._txt)):
            # if i % 2 == 0:
            for j in range(i, len(self._txt)):
                # j = i + 1
                logging.info("(i, j):->(%s, %s)" % (i, j))
                search_key = self._txt[i] + self._txt[j]
                if RedisClient.get_search_key(search_key):
                    continue
                try:
                    self._refresh_proxy()
                    self.proxy_search(search_key)
                    RedisClient.set_search_key(search_key)
                except Exception, e:
                    logging.exception("_run->%s" % e)
                    raise e
                    # continue

    def _run_2(self):
        all_count = QianzhanDB.get_all_count()
        self._refresh_proxy()
        for i in range(300000, all_count):
            item = QianzhanDB.get_one(i)
            search_key = item['company_name']
            logging.info("++++++++count_num -> %s , search_key -> %s++++++++++" % (i, search_key))
            if RedisClient.get_search_key(search_key):
                continue
            try:
                self.proxy_search(search_key)
                RedisClient.set_search_key(search_key)
            except Exception, e:
                logging.exception("_run->%s" % e)
                raise e
                # continue

    def _refresh_proxy(self):
        self._getProxy.remove_proxy(self._proxy_ip, self._proxy_port)
        self._proxy_ip, self._proxy_port, proxy_type = self._getProxy.get_proxy()
        proxies = "http://%s:%s" % (self._proxy_ip, self._proxy_port)
        logging.info("++++++++proxies: %s++++++++++++" % proxies)
        self._client = SiteClient(proxies)

    def proxy_search(self, search_key):

        try:
            self.search(search_key)
        except Error302, err:
            logging.error(err.message)
            self._refresh_proxy()
        except Error403, err:
            logging.error(err.message)
            self._refresh_proxy()
            self.proxy_search(search_key)
        except Error404, err:
            logging.error(err.message)
            self._refresh_proxy()
            self.proxy_search(search_key)
        except Error502, err:
            logging.error(err.message)
            self._refresh_proxy()
            self.proxy_search(search_key)
        except Error503, err:
            logging.error(err.message)
            self._refresh_proxy()
            self.proxy_search(search_key)
        except ErrorStatusCode, err:
            logging.error(err.message)
            self._refresh_proxy()
            self.proxy_search(search_key)
        except HttpClientError, err:
            logging.error(err.message)
            self._refresh_proxy()
            self.proxy_search(search_key)
        except MoreCheckverifyCodeTimesError, err:
            logging.error(err.message)
            self._refresh_proxy()
            self.proxy_search(search_key)
        except NeedrefreshProxyError, err:
            logging.error(err.message)
            # self._getProxy.remove_proxy(err._proxy_ip, err._proxy_port)
            self._refresh_proxy()
            self.proxy_search(search_key)
        except Exception, e:
            logging.exception(e)
            self._refresh_proxy()
            self.proxy_search(search_key)
            # raise e
            pass

    def search(self, search_key):
        # logging.info("search_key:->%s" % search_key)
        if RedisClient.get_search_key(search_key):
            return
        try:
            self.get_search(search_key)
            RedisClient.set_search_key(search_key)
        except UnknownTitle, e:
            raise e
        except UnicodeEncodeError, e:
            logging.exception(e)

    def get_search(self, search_key):
        response = self._client.get_search_list(search_key)
        # return response
        soup = BeautifulSoup(response.text, 'lxml')

        td_list = soup.find_all('td', attrs={"align": "left", "bgcolor": "#FFFFFF"})
        i = 1
        url = None  # url
        number = None  # 纳税人识别号
        company_name = None
        legal_person = None  # 法定代表人
        logging.info("td len:->%d" % len(td_list))
        for td in td_list:
            if i == 1:
                # print i, td
                onclick = td.select_one('a')['onclick']
                # javascript:window.open('queryto.jsp?nsrsbh=91110105MA003TH355','newwindow')
                url = onclick.split("'")[1]
                url = "http://www.bjsat.gov.cn/WSBST/bsdt/swdjzcx/" + url
                number = td.select_one('a').text
                i += 1
                pass
            elif i == 2:
                company_name = td.text
                # print i, td
                i += 1
                pass
            elif i == 3:
                legal_person = td.text
                try:
                    self.get_detail(url, number, company_name, legal_person)
                except Exception, e:
                    logging.exception(e)
                # print i, td
                i = 1
                pass
        pass

    def get_detail(self, url, number, company_name, legal_person):
        logging.info("%s, %s, %s, %s" % (url, number, company_name, legal_person))
        if RedisClient.get_result_url_key(url):
            return
        response = self._client.get_detail(url)
        soup = BeautifulSoup(response.text, 'lxml')
        tr_list = soup.select('table')[0].select('tr')
        company = {
            "url": url,
            "number": number,
            "company_name": company_name,
            "legal_person": legal_person
        }
        for tr in tr_list:
            td_list = tr.select('td')
            title = td_list[0].text.replace(' ', '').replace('\n', '').replace('\t', '').replace('\r', '').replace(
                u'\xa0', u'')
            value = td_list[1].text.replace(' ', '').replace('\n', '').replace('\t', '').replace('\r', '').replace(
                u'\xa0', u'')
            # logging.info("tr: %s" % tr)
            logging.info("%s:%s" % (title, value))
            if title == u"纳税人名称：":
                company.update({"company_name": value})
                pass
            elif title == u"法定代表人(负责人)：":
                company.update({"legal_person": value})
                pass
            elif title == u"地址：":
                company.update({"address": value})
                pass
            elif title == u"登记注册类型：":
                company.update({"type_of_registration": value})
                pass
            elif title == u"经营范围：":
                company.update({"business_scope": value})
                pass
            elif title == u"批准设立机关：":
                company.update({"approval_of_the_establishment_of_organs": value})
                pass
            elif title == u"扣缴义务：":
                company.update({"withholding": value})
                pass
            elif title == u"纳税人状态：":
                company.update({"taxpayer_status": value})
                pass
            elif title == u"增值税纳税人类别：":
                company.update({"category_of_value_added_tax": value})
                pass
            elif title == u"发证日期：":
                company.update({"date_of_issue": value})
                pass
            else:
                # print title
                raise UnknownTitle(title)
                pass
        BjsatDB.upsert_result(company)
        RedisClient.set_result_url_key(url)
        pass
