# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import time
import urllib
import logging
from PIL import Image
from bs4 import BeautifulSoup
from urlparse import urljoin

from mongo import QyxybaicDB, ProxyDB
from exception import Error302, Error403, Error400, Error404
from mredis import RedisClient
from captcha import read_img_file_to_string
from web_driver import new_webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from config import max_thread_num
import threadpool
from utils import get_1000_txt
from get_proxy import GetProxy
from selenium.common.exceptions import TimeoutException
from config import host, domain

class Spider(object):
    def __init__(self):
        self._txt = get_1000_txt()
        self._webdriver = None
        self._getProxy = GetProxy()
        pass

    def run(self):

        # for i in range(0, len(self._txt)):
        #     for j in range(i, len(self._txt)):
        #
        # logging.info("time:->" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        # pool = threadpool.ThreadPool(max_thread_num)
        # logging.info("time:->" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        # reqs = threadpool.makeRequests(self.search, search_keys)
        # logging.info("time:->" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        # [pool.putRequest(req) for req in reqs]
        # logging.info("time:->" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        # pool.wait()
        # logging.info("time:->" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        # # self.search()
        self._run()
        pass

    def _run(self):
        for i in range(0, len(self._txt)):
            if i % 2 == 0:
                j = i + 1
                logging.info("(i, j):->(%s, %s)" % (i, j))
                search_key = self._txt[i] + self._txt[j]
                try:
                    self.search(search_key)
                except Exception, e:
                    logging.exception("_run->%s" % e)
                    continue

    def search(self, search_key):
        logging.info("search-------->------>%s" % search_key)
        if RedisClient.get_search_key(search_key):
            return
        proxy_ip, proxy_port, proxy_type = self._getProxy.get_proxy()
        # proxy_ip, proxy_port, proxy_type = ('', '', '')
        try:
            logging.info("--->proxy->:--------> %s://%s:%s" % (proxy_type, proxy_ip, proxy_port))
            if self._webdriver:
                self._webdriver.close()
                self._webdriver = None
            self._webdriver = new_webdriver(proxy_type, proxy_ip, proxy_port)
            self._search(search_key)
            # self._webdriver.close()
            # self._webdriver = None
            RedisClient.set_search_key(search_key)
        except TimeoutException, e:
            logging.info("<---------search timeout .....----------->")
            ProxyDB.remove_proxy(proxy_ip, proxy_port)
            self.search(search_key)

    def _search(self, search_key):
        logging.info("_search+++++%s" % search_key)
        # 访问首页
        self._webdriver.get(domain)
        WebDriverWait(self._webdriver, 60 * 1).until(EC.visibility_of_element_located((By.NAME, "topFrame")))
        # time.sleep(2)
        # 切换到主frame
        self._webdriver.switch_to.frame("topFrame")
        WebDriverWait(self._webdriver, 60 * 1).until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
        # 关闭弹窗
        float_img_x = self._webdriver.find_element_by_xpath('//div[@id="float_icon"]/div/img')
        float_img_x.click()
        time.sleep(1)
        # 输入关键字, 开始搜索
        key_word_input = self._webdriver.find_element_by_id('key_word')
        search_button = self._webdriver.find_element_by_xpath('//h3/a')
        key_word_input.clear()
        key_word_input.send_keys(search_key)
        search_button.click()  # search
        WebDriverWait(self._webdriver, 60 * 1).until(EC.visibility_of_element_located((By.ID, "MzImgExpPwd")))
        time.sleep(1)
        # 处理验证码弹窗
        code_img = self._webdriver.find_element_by_id('MzImgExpPwd')
        text_field = self._webdriver.find_element_by_id('textfield')
        search_button_2 = self._webdriver.find_element_by_xpath('//table[@class="k-00-c"]/tbody/tr/td/div/a')
        # 处理验证码
        while True:
            self._webdriver.save_screenshot('1.png')
            im = Image.open('1.png')
            region = im.crop((code_img.location['x'],
                              code_img.location['y'],
                              code_img.location['x'] + code_img.size['width'],
                              code_img.location['y'] + code_img.size['height']))  # 这里用int,否则linux上会报错
            region = region.resize((200, 50), Image.ANTIALIAS)
            region.save('2.png')
            code = read_img_file_to_string('2.png')
            if code != '':
                text_field.clear()
                text_field.send_keys(code)
                search_button_2.click()
                time.sleep(2)
                try:
                    logging.info("search_button click...")
                    # 错误弹窗处理
                    alert = self._webdriver.switch_to.alert
                    logging.info("alert %s" % alert)
                    if alert:
                        alert.accept()
                        time.sleep(1)
                        logging.info("alert accept.............")
                        # h = self._webdriver.window_handles[0]
                        # self._webdriver.switch_to.window(h)
                        # self._webdriver.switch_to.frame("topFrame")
                        code_img = self._webdriver.find_element_by_id('MzImgExpPwd')
                        # text_field = self._webdriver.find_element_by_id('textfield')
                        # search_button_2 = self._webdriver.find_element_by_xpath('//table[@class="k-00-c"]/tbody/tr/td/div/a')
                        code_img.click()
                        time.sleep(1)
                        continue
                    else:
                        break
                except Exception, e:
                    # 没有错误弹窗
                    # logging.exception(e)
                    break
            else:
                code_img.click()
                time.sleep(3)
                continue

        try:
            self.next_page()
        except TimeoutException, e:
            logging.exception(e)
            raise e
            # except Exception, e:
            #     logging.exception("next_page->%s" % e)

    def next_page(self):
        logging.info("<--------------+++++++++next page...............+++++++++++------->")
        WebDriverWait(self._webdriver, 40 * 1).until(EC.visibility_of_element_located((By.CLASS_NAME, "bx1")))
        # 处理公司列表
        a_list = self._webdriver.find_elements_by_xpath('//div[@class="bx1"]/table/tbody/tr/td/font/a')
        a_list_len = len(a_list)
        logging.info("a_list len:->--->--->---- %s ----<<<--<-<" % a_list_len)
        logging.info("for a in a_list.....begin......")
        for a in a_list:

            onclick = a.get_attribute("onclick")
            logging.info("onclick---->-->%s" % onclick)
            reg_bus_ent_id = onclick.split('reg_bus_ent_id=')[1].split('&')[0]
            if RedisClient.get_reg_bug_ent_id(reg_bus_ent_id):
                continue

            try:
                a.click()
                while len(self._webdriver.window_handles) != 2:
                    time.sleep(1)
                h = self._webdriver.window_handles[1]
                self._webdriver.switch_to.window(h)  # 子窗口
                self.do_company_detail_window(reg_bus_ent_id)
                self._webdriver.close()  # 关闭子窗口

                RedisClient.set_reg_bug_ent_id(reg_bus_ent_id)
            except TimeoutException, e:
                logging.exception(e)
                raise e
            except Exception, e:
                logging.exception("parse_detail_window->%s" % e)

            self._webdriver.switch_to.window(self._webdriver.window_handles[0])  # 回到搜索页面
            self._webdriver.switch_to.frame("topFrame")

        logging.info("for a in a_list.....end......")
        if a_list_len < 10:
            return
        try:
            # 翻页
            tr = self._webdriver.find_elements_by_xpath('//div[@class="bx1"]/table/tbody/tr')[-1]
            next_page = tr.find_element_by_xpath('./td/a[3]')
            next_page.click()
            time.sleep(2)
            self.next_page()
        except TimeoutException, e:
            logging.exception(e)
            raise e
            # except Exception, e:
            #     logging.exception("next_page->%s" % e)

    # 处理公司详情
    def do_company_detail_window(self, reg_bus_ent_id):
        logging.info("do_company_detail_window->..................")
        WebDriverWait(self._webdriver, 60 * 1).until(EC.visibility_of_element_located((By.CLASS_NAME, "main")))

        company = {"reg_bus_ent_id": reg_bus_ent_id}

        # company = self.do_leftmain(company)
        company = self.do_main(company)

        # insert to mongodb
        try:
            company.update({'company_name': company['base_info']['gsdjzc_info']['name']})
        except Exception, e:
            pass
        QyxybaicDB.upsert_company(company)
        # RedisClient.set_company_url_detail_key()

    def do_leftmain(self, company):
        # TODO do leftMain
        logging.info("do left main..........")
        tzr_list_duo = self._webdriver.find_element_by_xpath(
            '//div[@class="main"]/div[@class="leftMain"]/div[@id="tzrlistThree"][1]/div[@class="cha-1-duo"]/a')
        logging.info("tzr_list_duo ..........%s" % tzr_list_duo)
        tzr_list_duo.click()
        logging.info("click............")
        while len(self._webdriver.window_handles) != 3:
            time.sleep(1)
        h = self._webdriver.window_handles[2]
        self._webdriver.switch_to.window(h)  # 子窗口
        company.update({
            "tzr_list": self.do_tzr_list_window()
        })
        self._webdriver.close()  # 关闭子窗口
        self._webdriver.switch_to.window(self._webdriver.window_handles[1])  # 回到详情页面

        tzr_history_list_duo = self._webdriver.find_element_by_xpath(
            '//div[@class="main"]/div[@class="leftMain"]/div[@class="cha-1"][2]/div[@class="cha-1-duo"]/a')
        tzr_history_list_duo.click()
        h = self._webdriver.window_handles[2]
        self._webdriver.switch_to.window(h)  # 子窗口
        company.update({
            "tzr_history_list": self.do_tzr_history_list_window()
        })
        self._webdriver.switch_to.window(self._webdriver.window_handles[1])  # 回到详情页面

        zyry_list_duo = self._webdriver.find_element_by_xpath(
            '//div[@class="main"]/div[@class="leftMain"]/div[@class="cha-2"][1]/div[@class="cha-1-duo-0"]/div[@class="cha-1-duo"]/a')
        zyry_list_duo.click()
        # while len(self._webdriver.window_handles) != 3:
        #     time.sleep(1)
        h = self._webdriver.window_handles[2]
        self._webdriver.switch_to.window(h)  # 子窗口
        company.update({
            "zyry_list": self.do_zyry_list_window()
        })
        self._webdriver.close()  # 关闭子窗口
        self._webdriver.switch_to.window(self._webdriver.window_handles[1])  # 回到详情页面

        bgxx_list_duo = self._webdriver.find_element_by_xpath(
            '//div[@class="main"]/div[@class="leftMain"]/div[@class="cha-2"][2]/div[@class="cha-1-duo-0"]/span')
        bgxx_list_duo.click()
        h = self._webdriver.window_handles[2]
        self._webdriver.switch_to.window(h)  # 子窗口
        company.update({
            "bgxx_list": self.do_bgxx_list_window()
        })
        self._webdriver.switch_to.window(self._webdriver.window_handles[1])  # 回到详情页面

        # TODO 分支机构
        # TODO 再投资信息
        return company
        pass

    def do_main(self, company):
        logging.info("do_main...............")
        # TODO do main
        page_source = self._webdriver.page_source
        soup = BeautifulSoup(page_source, 'lxml')

        # main_tag = soup.select_one('div[class="main"]')

        company.update({"base_info": self.parse_base_info(soup)})

        # TODO 其他信息
        company.update({
            "other_info": self.parse_other_info()
        })

        # TODO 公司公示信息
        company.update({
            "gsgs_info": self.parse_gsgs_info()
        })

        return company

    def parse_other_info(self):
        logging.info("parse_other_info...............")
        other_info = {}
        return other_info

    def parse_gsgs_info(self):
        logging.info("parse_gsgs_info...............")
        gsgs_info = {}
        # 企业年报
        self._webdriver.switch_to.frame('qynbFrame')
        try:
            WebDriverWait(self._webdriver, 40 * 1).until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
            a_2015 = self._webdriver.find_elements_by_xpath('//table/tbody/tr/td/a')[-1]
            a_2015.click()
            while len(self._webdriver.window_handles) != 3:
                time.sleep(1)
            h = self._webdriver.window_handles[2]
            self._webdriver.switch_to.window(h)  # 子窗口
            gsgs_info.update({
                "qynb_info": self.do_qynb_window()
            })
            self._webdriver.close()  # 关闭子窗口
            self._webdriver.switch_to.window(self._webdriver.window_handles[1])  # 回到详情页面
        except TimeoutException, e:
            logging.exception(e)
            raise e
        except Exception, e:
            logging.exception("parse_gsgs_info.....e: %s" % e)

        return gsgs_info



    def do_tzr_list_window(self):
        logging.info("do_tzr_list_window..............")
        # 处理投资人信息
        tzr_list = []

        page_source = self._webdriver.page_source
        soup = BeautifulSoup(page_source, 'lxml')
        tr_list = soup.select('table[id="tableIdStyle"] tbody tr')
        for tr in tr_list[1:-1]:
            td_list = tr.select('td')
            investor = {}
            investor.update({
                "number": td_list[0].getText(),  # 序号
                "name": td_list[1].getText(),  # 投资人名称
                "investor_type": td_list[2].getText(),  # 投资人类型
                "card_type": td_list[3].getText(),  # 证照类型
                "card_number": td_list[4].getText()  # 证照号码
            })
            tzr_list.append(investor)

        return tzr_list

    def do_tzr_history_list_window(self):
        logging.info("do_tzr_history_list_window..............")
        # 处理投资人历史信息
        tzr_history_list = []

        page_source = self._webdriver.page_source
        soup = BeautifulSoup(page_source, 'lxml')
        tr_list = soup.select('table[id="tableIdStyle"] tbody tr')
        for tr in tr_list[1:-1]:
            td_list = tr.select('td')
            investor = {}
            investor.update({
                "number": td_list[0].getText(),  # 序号
                "name": td_list[1].getText(),  # 投资人名称
                "investor_type": td_list[2].getText(),  # 投资人类型
                "card_type": td_list[3].getText(),  # 证照类型
                "card_number": td_list[4].getText()  # 证照号码
            })
            tzr_history_list.append(investor)

        return tzr_history_list

    def do_zyry_list_window(self):
        logging.info("do_zyry_list_window..............")
        # 处理主要人员信息
        zyry_list = []

        page_source = self._webdriver.page_source
        soup = BeautifulSoup(page_source, 'lxml')
        tr_list = soup.select('table[id="tableIdStyle"] tbody tr')
        for tr in tr_list[1:-1]:
            td_list = tr.select('td')
            people = {}
            people.update({
                "number": td_list[0].getText(),  # 序号
                "name": td_list[1].getText(),  # 姓名
                "position": td_list[2].getText(),  # 职位
                "sex": td_list[3].getText(),  # 性别

            })
            zyry_list.append(people)

        return zyry_list

    def do_bgxx_list_window(self):
        logging.info("do_bgxx_list_window..............")
        # 处理变更信息
        bgxx_list = []
        return bgxx_list


    def parse_base_info(self, soup):
        logging.info("parse_base_info..............")
        #  基础信息
        base_info = {}

        try:
            table_list = soup.select('div[class="jic"] table')
            for i in range(1, len(table_list) / 2 + 1):
                f_lan_index = 2 * i - 2
                f_lan_table = table_list[f_lan_index]
                f_lbiao_table = table_list[f_lan_index + 1]
                text = f_lan_table.select_one('tbody tr td').getText().strip()
                text = text.strip()

                if text == u"工商登记注册基本信息":
                    base_info.update({"gsdjzc_info": self.parse_gsdjzc_info(f_lbiao_table)})  # 工商登记注册基本信息
                    pass
                elif text == u"资本相关信息":
                    base_info.update({"zbxg_info": self.parse_zbxg_info(f_lbiao_table)})  # 资本相关信息
                    pass
                elif text == u"组织机构代码信息":
                    base_info.update({"zzjgdm_info": self.parse_zzjgdm_info(f_lbiao_table)})  # 组织机构代码信息
                    pass
                elif text == u"税务登记信息":
                    base_info.update({"swdj_info": self.parse_swdj_info(f_lbiao_table)})  # 税务登记信息
                    pass
                else:
                    logging.error("unknown text ->%s" % text)
                    exit(1)
        except Exception, e:
            logging.exception("parse_base_info->%s" % e)

        return base_info

    def parse_gsdjzc_info(self, f_lbiao_table):
        logging.info("parse_gsdjzc_info..............")
        # 解析工商登记注册基本信息
        gsdjzc_info = {}

        # table_list = soup.select('div[class="jic"] table')
        # table = table_list[1]
        # td_list = table.select('tbody tr td')

        try:
            td_list = f_lbiao_table.select('tbody tr td')
            # logging.info(td_list)
            # gsdjzc_info.update({
            #     "name": td_list[1].getText(),  # 名称
            #     "unified_social_credit_code": td_list[3].getText(),  # 统一社会信用代码
            #     "type": td_list[5].getText(),  # 类型
            #     "legal_representative": td_list[7].getText(),  # 法定代表人
            #     "date_of_establishment": td_list[9].getText(),  # 成立日期
            #     "address": td_list[11].getText(),  # 住所
            #     "operating_period_begin": td_list[13].getText(),  # 营业期限自
            #     "operating_period_end": td_list[15].getText(),  # 营业期限至
            #     "business_scope": td_list[17].getText(),  # 经营范围
            #     "registration_authority": td_list[19].getText(),  # 登记机关
            #     "approved_date": td_list[21].getText(),  # 核准日期
            #     "registration_status": td_list[23].getText(),  # 登记状态
            # })
            #
            # key_value = {
            #     u"名称：": "name",
            #     u"统一社会信用代码：": "unified_social_credit_code",
            #     u"注册号：": "registration_number",
            #
            #     u"法定代表人：": "legal_representative",
            #     u"经营者：": "operator",
            #     u"经营者姓名：": "operator",
            #     u"负责人：": "responsible_person",
            #
            #     u"投资人姓名：": "investor",
            #
            #     u"类型：": "company_type",
            #     u"公司类型：": "company_type",
            #
            #     u"企业状态：": "business_status",
            #     u"登记状态：": "business_status",
            #     u"状态：": "business_status",
            #
            #     u"经营范围：": "business_scope",
            #     u"营业期限自：": "operating_period_begin",
            #     u"营业期限至：": "operating_period_end",
            #
            #     u"成立日期：": "register_date",
            #     u"注册日期：": "register_date",
            #     u"核准日期：": "register_date",
            #     u"发照日期：": "register_date",
            #
            #     u"吊销日期：": "revocation_date",
            #     u"注销日期：": "cancellation_date",
            #
            #     u"登记机关：": "registration_authority",
            #     u"发照机关：": "registration_authority",
            #
            #     u"经营场所：": "address",
            #     u"营业场所：": "address",
            #     u"住所：": "address",
            #     u"企业住所：": "address",
            #
            #     u"组成形式：": "composition_form",
            #
            #     u"注册资本：": "registered_capital",
            #     u"经济性质：": ""
            # }
            for i in range(0, len(td_list) / 2):
                td_1 = td_list[i * 2]
                td_2 = td_list[i * 2 + 1]
                key = td_1.select_one('div').getText().replace(' ', '').replace('\n', '').replace('\t', '').replace('：',
                                                                                                                    '')
                value = td_2.getText().strip()
                try:
                    gsdjzc_info.update({key: value})
                except Exception, e:
                    logging.error("unknown key: %s" % key)
                    exit(1)

        except Exception, e:
            logging.exception("parse_gsdjzc_info->%s" % e)

        return gsdjzc_info

    def parse_zbxg_info(self, f_lbiao_table):
        logging.info("parse_zbxg_info..............")
        # 解析资本相关信息
        gsdjzc_info = {}
        try:
            td_list = f_lbiao_table.select('tbody tr td')
            # key_value = {
            #     u"注册资本：": "registered_capital",
            #     u"实收资本：": "paid_in_capital",
            #     u"公司公示信息": "-",
            #     u"实缴出资金额：": "the_amount_of_investment_actually_paid",
            #     u"最终实缴出资时间：": "the_final_paid_off_investment_time",
            #     u"最终认缴出资时间：": "the_final_subscribed_funding_time",
            #     u"-": "-"
            # }
            for i in range(0, len(td_list) / 2):
                td_1 = td_list[i * 2]
                td_2 = td_list[i * 2 + 1]
                try:
                    key = td_1.select_one('div').getText().strip()
                except Exception, e:
                    key = u"-"
                value = td_2.getText().strip()
                try:
                    gsdjzc_info.update({key: value})
                except Exception, e:
                    logging.error("unknown key: %s" % key)
                    exit(1)
        except Exception, e:
            logging.exception("parse_zbxg_info->%s" % e)

        return gsdjzc_info

    def parse_zzjgdm_info(self, f_lbiao_table):
        logging.info("parse_zzjgdm_info..............")
        # 解析组织机构代码信息
        zzjgdm_info = {}
        try:
            td_list = f_lbiao_table.select('tbody tr td')
            # key_value = {
            #     u"组织机构代码：": "organization_code",
            #     u"代码证颁发机关：": "code_certification_authority"
            # }
            for i in range(0, len(td_list) / 2):
                td_1 = td_list[i * 2]
                td_2 = td_list[i * 2 + 1]
                key = td_1.select_one('div').getText().strip()
                value = td_2.getText().strip()
                try:
                    zzjgdm_info.update({key: value})
                except Exception, e:
                    logging.error("unknown key: %s" % key)
                    exit(1)
        except Exception, e:
            logging.exception("parse_zzjgdm_info->%s" % e)

        return zzjgdm_info

    def parse_swdj_info(self, f_lbiao_table):
        logging.info("parse_swdj_info..............")
        # 解析税务登记信息
        gsdjzc_info = {}
        try:
            th_list = f_lbiao_table.select('tbody tr th')
            td_list = f_lbiao_table.select('tbody tr td')
            for i in range(0, len(th_list)):
                th_text = th_list[i].getText().strip().replace('：', '')
                td_text = td_list[i].getText().strip()
                gsdjzc_info.update({th_text: td_text})
                # if th_text == u"纳税人名称：":
                #     gsdjzc_info.update({"name_of_taxpayer": td_text})
                # elif th_text == u"税务登记类型：":
                #     gsdjzc_info.update({"tax_registration_type": td_text})
                # elif th_text == u"税务登记证号：":
                #     gsdjzc_info.update({"tax_registration_number": td_text})
                # elif th_text == u"注册号：":
                #     gsdjzc_info.update({"registration_number": td_text})
                # elif th_text == u"法人姓名：":
                #     gsdjzc_info.update({"corporate_name": td_text})
                # elif th_text == u"组织机构代码：":
                #     gsdjzc_info.update({"organization_code": td_text})
                # elif th_text == u"登记受理类型：":
                #     gsdjzc_info.update({"registration_type": td_text})
                # elif th_text == u"经营地址：":
                #     gsdjzc_info.update({"business_address": td_text})
                # elif th_text == u"经营地址联系电话：":
                #     gsdjzc_info.update({"business_address_contact_phone": td_text})
                # elif th_text == u"经营地址邮编：":
                #     gsdjzc_info.update({"business_address_zip_code": td_text})
                # elif th_text == u"企业主页网址：":
                #     gsdjzc_info.update({"enterprise_web_site": td_text})
                # elif th_text == u"所处街乡：":
                #     gsdjzc_info.update({"the_street_township": td_text})
                # elif th_text == u"国地税共管户标识：":
                #     gsdjzc_info.update({"national_land_tax_co_management_identity": td_text})
                # elif th_text == u"登记注册类型：":
                #     gsdjzc_info.update({"type_of_registration": td_text})
                # elif th_text == u"隶属关系：":
                #     gsdjzc_info.update({"subordinate_relationship": td_text})
                # elif th_text == u"国家标准行业：":
                #     gsdjzc_info.update({"national_standard_industry": td_text})
                # elif th_text == u"税务登记日期：":
                #     gsdjzc_info.update({"date_of_tax_registration": td_text})
                # elif th_text == u"主管税务机关：":
                #     gsdjzc_info.update({"competent_tax_authority": td_text})
                # elif th_text == u"纳税人状态：":
                #     gsdjzc_info.update({"taxpayer_status": td_text})
                # else:
                #     logging.error("unknown th_text -> %s" % th_text)
                #     exit(1)
        except Exception, e:
            logging.exception("parse_swdj_info->%s" % e)

        return gsdjzc_info

    def do_qynb_window(self):
        logging.info("do_qynb_window...............")
        qynb_info = {}
        try:
            # 企业年报
            WebDriverWait(self._webdriver, 60 * 1).until(EC.visibility_of_element_located((By.ID, "details")))

            base_info = {}
            page_source = self._webdriver.page_source
            soup = BeautifulSoup(page_source, 'lxml')
            table = soup.select_one('table')
            tr_list = table.select('tbody tr')
            for tr in tr_list:
                th_list = tr.select('th')
                td_list = tr.select('td')
                if len(td_list) > 0:
                    for i in range(0, len(td_list)):
                        td = td_list[i]
                        th = th_list[i]
                        key = th.getText().strip()
                        value = td.getText().strip()
                        base_info.update({key: value})

                        # if key == u"注册号/统一社会信用代码":
                        #     base_info.update({"unified_social_credit_code": value})
                        # elif key == u"企业名称":
                        #     base_info.update({"company_name": value})
                        # elif key == u"企业联系电话":
                        #     base_info.update({"phone": value})
                        # elif key == u"邮政编码":
                        #     base_info.update({"zip_code": value})
                        # elif key == u"企业通信地址":
                        #     base_info.update({"address": value})
                        # elif key == u"电子邮箱":
                        #     base_info.update({"email": value})
                        # elif key == u"有限责任公司本年度是否发生股东股权转让":
                        #     base_info.update({"is_equity_transfer": value})
                        # elif key == u"企业经营状态":
                        #     base_info.update({"business_status": value})
                        # elif key == u"是否有网站或网店":
                        #     base_info.update({"is_have_website": value})
                        # elif key == u"企业是否有投资信息或购买其他公司股权":
                        #     base_info.update({"is_have_tzxx": value})
                        # elif key == u"从业人数":
                        #     base_info.update({"people_num": value})
                        # elif key == u"":
                        #     base_info.update({"-": value})
                        # else:
                        #     logging.error("unknown key:%s" % key)
                        #     exit(1)
                        #     pass

            qynb_info.update({"base_info": base_info})
        except TimeoutException, e:
            logging.exception(e)
            raise e
        except Exception, e:
            logging.exception("do_qynb_window->e:%s" % e)

        return qynb_info
