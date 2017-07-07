# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import time
import urllib
import logging
import time
from bs4 import BeautifulSoup
from urlparse import urljoin

from mongo import QianlimaDB
from exception import Error302, Error403, Error400, Error404
from mredis import RedisClient
from captcha import read_img_file_to_string
from web_driver import new_webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Spider(object):
    def __init__(self, username, password):
        # self._site_client = SiteClient(userId, password)
        self._username = username
        # self._userId = userId
        self._password = password
        self._webdriver = new_webdriver()
        # self._list_window_handle = None

        self._count = 0
        pass

    def login(self):
        logging.info("login++++++")
        login_page_url = "http://center.qianlima.com/login.jsp"
        self._webdriver.get(login_page_url)
        # time.sleep(60 * 2)
        username_input = WebDriverWait(self._webdriver, 60 * 2).until(EC.element_to_be_clickable((By.NAME, "username")))
        password_input = WebDriverWait(self._webdriver, 40).until(EC.element_to_be_clickable((By.NAME, "password")))
        loginform_button = WebDriverWait(self._webdriver, 40).until(EC.element_to_be_clickable((By.ID, "deng")))
        # username_input = self._webdriver.find_element_by_id('abc')
        # password_input = self._webdriver.find_element_by_name('password')
        # verifycode_input = self._webdriver.find_element_by_id('verifycode')
        # loginform_button = self._webdriver.find_element_by_id('deng')
        # code_img = self._webdriver.find_element_by_class_name('code-img')

        # screen_shot_file = 'screen_shot.png'
        # self._webdriver.save_screenshot(screen_shot_file)
        # code = read_img_file_to_string(screen_shot_file, code_img.location['x'], code_img.location['y'],
        #                                code_img.size['width'], code_img.size['height'])
        #
        logging.debug("after get login_url+++++")
        username_input.click()
        username_input.send_keys(self._username)
        password_input.clear()
        password_input.send_keys(self._password)
        # verifycode_input.send_keys(code)

        loginform_button.click()
        WebDriverWait(self._webdriver, 60 * 1).until(EC.presence_of_element_located((By.CLASS_NAME, "my-content")))

        pass

    def search(self):
        logging.info("search+++++")
        # searchname_input = self._webdriver.find_element_by_id('searchname')
        # searchname_input.send_keys(search_key)
        # search_button = self._webdriver.find_element_by_class_name('sec-btn')
        # search_button.click()

        # url = 'http://search.qianlima.com/qlm_adv_se.jsp?kw1=&kw2=&kw3=&field=0&p_tflt=365&q_time_start=2015-08-30&q_time_end=2016-08-29&iarea=0&area=2&prg=0%3D3&x=71&y=12'
        # self.next_page(url)

        for i in range(1, 3901):
            logging.info("i+++++++++++++++%s" % i)
            next_url = "http://search.qianlima.com/qlm_adv_se.jsp?p=" + str(
                i) + "&kw1=&kw2=&kw3=&field=0&p_tflt=365&q_time_start=2013-01-01&q_time_end=2016-08-29&area=2&prg=0%3D3"
            try:
                self.next_page(next_url)
            except Exception, e:
                logging.exception(e)
                raise Exception("error")
                pass

    def next_page(self, url):
        logging.info("next_page+++++%s" % url)
        # self._list_window_handle = self._webdriver.current_window_handle
        self._webdriver.get(url)
        # time.sleep(60)
        WebDriverWait(self._webdriver, 60 * 1).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="two_line"]/a')))
        page_source = self._webdriver.page_source
        #     self.parse_list_page_source(page_source)
        #
        # def parse_list_page_source(self, page_source):
        #     logging.info("parse_list_page_source........")
        # logging.debug(page_source)
        soup = BeautifulSoup(page_source, 'lxml')

        a_list = soup.select('div[class="two_line"] a')
        # logging.info(a_list)
        for a in a_list:
            detail_url = a['href']
            try:
                self.detail(detail_url)
            except Exception, e:
                logging.exception(e)
                raise Exception("error")
                pass
            # font = soup.select_one('font[color="red"]')
            # next_page = font.next_sibling['href']
            # self.next_page(next_page)

    def detail(self, detail_url):
        if RedisClient.get_company_url_detail_key(detail_url):
            return
        logging.info("detail+++++%s" % detail_url)
        self._webdriver.get(detail_url)
        # time.sleep(20)
        WebDriverWait(self._webdriver, 60 * 1).until(
            EC.visibility_of_element_located((By.ID, "wen")))
        page_source = self._webdriver.page_source
        # logging.debug(page_source)
        #     self.parse_detail_page_source(page_source)
        #
        # def parse_detail_page_source(self, page_source):
        #     logging.info("parse_detail_page_source........")

        soup = BeautifulSoup(page_source, 'lxml')

        title = soup.select_one('div[class="wenshang"] h2').getText()
        update_time = soup.select('div[class="wenzhong"] div[class="biaoge"] table tr')[1].select_one(
            'td span').getText()
        detail = soup.select_one('div[id="wen"]').renderContents()

        self._count += 1
        logging.info("++++++count++++++++++%s" % self._count)
        QianlimaDB.upsert_company({
            "title": title,
            "update_time": update_time,
            "detail": detail,
            "url": detail_url
        })

        # txt_line_list = soup.text.split('\n')
        # new_list = []
        # for line in txt_line_list:
        #     l = line.split(' ')
        #     for ll in l:
        #         new_list.append(ll)
        #
        # company_name_list = []
        #
        # for line in new_list:
        #     line = line.strip()
        #     text = line.replace(u'：', u':')
        #
        #     if text.find(u'采购单位名称:') > -1:
        #         company_name = text[text.find(u'采购单位名称：') + len(u'采购单位名称:'):]
        #         if company_name not in company_name_list:
        #             company_name_list.append(company_name)
        #     if text.find(u'采购代理机构全称:') > -1:
        #         company_name = text[text.find(u'采购代理机构全称:') + len(u'采购代理机构全称:'):]
        #         if company_name not in company_name_list:
        #             company_name_list.append(company_name)
        #     if text.find(u'成交供应商名称:') > -1:
        #         company_name = text[text.find(u'成交供应商名称:') + len(u'成交供应商名称:'):]
        #         if company_name not in company_name_list:
        #             company_name_list.append(company_name)
        #     if text.find(u'中标供应商:') > -1:
        #         company_name = text[text.find(u'中标供应商:') + len(u'中标供应商:'):]
        #         if company_name not in company_name_list:
        #             company_name_list.append(company_name)
        #     if text.find(u'中标人:') > -1:
        #         company_name = text[text.find(u'中标人:') + len(u'中标人:'):]
        #         if company_name not in company_name_list:
        #             company_name_list.append(company_name)
        #     if text.find(u'推荐中标商:') > -1:
        #         company_name = text[text.find(u'推荐中标商:') + len(u'推荐中标商:'):]
        #         if company_name not in company_name_list:
        #             company_name_list.append(company_name)
        #     if text.find(u'招标机构:') > -1:
        #         company_name = text[text.find(u'招标机构:') + len(u'招标机构:'):]
        #         if company_name not in company_name_list:
        #             company_name_list.append(company_name)
        #     if text.find(u'招标代理机构:') > -1:
        #         company_name = text[text.find(u'招标代理机构:') + len(u'招标代理机构:'):]
        #         if company_name not in company_name_list:
        #             company_name_list.append(company_name)
        #     if text.find(u'招标人:') > -1:
        #         company_name = text[text.find(u'招标人:') + len(u'招标人:'):]
        #         if company_name not in company_name_list:
        #             company_name_list.append(company_name)
        #     if text.find(u'招标人名称:') > -1:
        #         company_name = text[text.find(u'招标人名称:') + len(u'招标人名称:'):]
        #         if company_name not in company_name_list:
        #             company_name_list.append(company_name)
        #     if text.endswith(u'公司') and text.find(u':') < 0:
        #         company_name = text
        #         if company_name not in company_name_list:
        #             company_name_list.append(company_name)
        #     if text.endswith(u'公司') and text.startswith(u'北京') < 0:
        #         company_name = text
        #         if company_name not in company_name_list:
        #             company_name_list.append(company_name)
        #     if text.find(u'公司') > -1:
        #         company_name = text[text.find(u'公司') - 8: text.find(u'公司')]
        #         if company_name not in company_name_list:
        #             company_name_list.append(company_name)
        #     if text.find(u'公司') > -1:
        #         company_name = text[text.find(u'公司') - 10: text.find(u'公司')]
        #         if company_name not in company_name_list:
        #             company_name_list.append(company_name)
        #
        # for company_name in company_name_list:
        #     # insert to mongodb
        #     QianlimaDB.upsert_company(company_name)
        #
        #     pass
        RedisClient.set_company_url_detail_key(detail_url)

    def run(self):
        self.login()
        # for i in range(100):
        # search_key = ''
        self.search()

        pass
