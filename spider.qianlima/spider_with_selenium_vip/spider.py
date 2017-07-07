# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

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
        province_list = [
            # {"page": 29173, "p_area": 1, "province": u"安徽"},
            # {"page": 36453, "p_area": 2, "province": u"北京"},
            # {"page": 30581, "p_area": 3, "province": u"福建"},
            # {"page": 8695, "p_area": 4, "province": u"甘肃"},
            {"page": 133026, "p_area": 5, "province": u"广东"},
            {"page": 26785, "p_area": 6, "province": u"广西"},
            {"page": 10725, "p_area": 7, "province": u"贵州"},
            {"page": 3203, "p_area": 8, "province": u"海南"},
            {"page": 75394, "p_area": 9, "province": u"河北"},
            {"page": 22111, "p_area": 10, "province": u"河南"},
            {"page": 13590, "p_area": 11, "province": u"黑龙江"},
            {"page": 24394, "p_area": 12, "province": u"湖北"},
            {"page": 27488, "p_area": 13, "province": u"湖南"},
            {"page": 9788, "p_area": 14, "province": u"吉林"},
            {"page": 71443, "p_area": 15, "province": u"江苏"},
            {"page": 12282, "p_area": 16, "province": u"江西"},
            {"page": 42944, "p_area": 17, "province": u"辽宁"},
            {"page": 10660, "p_area": 18, "province": u"内蒙古"},
            {"page": 2303, "p_area": 19, "province": u"宁夏"},
            {"page": 17988, "p_area": 20, "province": u"青海"},
            {"page": 60826, "p_area": 21, "province": u"山东"},
            {"page": 24918, "p_area": 22, "province": u"山西"},
            {"page": 16501, "p_area": 23, "province": u"陕西"},
            {"page": 61757, "p_area": 24, "province": u"上海"},
            {"page": 38447, "p_area": 25, "province": u"四川"},
            {"page": 26094, "p_area": 26, "province": u"天津"},
            {"page": 1989, "p_area": 27, "province": u"西藏"},
            {"page": 7808, "p_area": 28, "province": u"新疆"},
            {"page": 16268, "p_area": 29, "province": u"云南"},
            {"page": 89926, "p_area": 30, "province": u"浙江"},
            {"page": 15409, "p_area": 31, "province": u"重庆"},
        ]

        for obj in province_list:
            self._search(obj.get("page"), obj.get("p_area"), obj.get("province"))
        pass

    def _search(self, page_max, p_area, province):
        logging.info("search+++++")

        page_list = range(1, page_max + 500)
        page_list.reverse()
        for pg in page_list:
            logging.info("pg+++++++++++++++%s" % pg)

            try:
                self.next_page(pg, p_area, province)
            except Exception, e:
                logging.exception(e)
                time.sleep(60 * 1)
                pass

    def next_page(self, pg, p_area, province):
        next_url = "http://center.qianlima.com/db_qy.jsp?pg=" + str(pg) + "&p_area=" + str(
            p_area) + "&gsmc=null&lxrxm=null"
        if RedisClient.get_url_key(next_url):
            return
        logging.info("next_page+++++%s" % next_url)

        # self._list_window_handle = self._webdriver.current_window_handle
        self._webdriver.get(next_url)
        # time.sleep(60)
        WebDriverWait(self._webdriver, 60 * 1).until(
            EC.presence_of_element_located((By.XPATH, '//table[@class="gz-news pool"]/tbody/tr')))
        page_source = self._webdriver.page_source

        soup = BeautifulSoup(page_source, 'lxml')

        tr_list = soup.select('table[class="gz-news pool"] tbody tr')
        # logging.info(a_list)
        for tr in tr_list:
            td_list = tr.select('td')

            company = {
                "company_name": td_list[0].get_text(),
                "contact": td_list[1].get_text(),
                "phone": td_list[2].get_text(),
                "mobile": td_list[3].get_text(),
                "fax": td_list[4].get_text(),
                "address": td_list[5].get_text(),
                "describe": td_list[6].get_text(),
                "area": td_list[7].get_text(),
                "p_area": p_area,
                "province": province
            }
            QianlimaDB.upsert_company(company)

        # href = soup.select('form a')[-2].href
        # next_url = "http://center.qianlima.com/db_qy.jsp" + href
        # self.next_page(next_url, area_num)
        RedisClient.set_url_key(next_url)

    def close(self):
        self._webdriver.close()

    def run(self):
        self.login()
        # for i in range(100):
        # search_key = ''
        self.search()
        self.close()
        pass
