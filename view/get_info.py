import sys
import os
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

sys.path.append(os.pardir)
import const


class GetInfo:
    def __init__(self, scraping_manager, args):
        self.scraping_manager = scraping_manager
        self.driver = scraping_manager.driver
        self.args = args
        self.wait = WebDriverWait(scraping_manager.driver, 5)
        self.top_url = self.get_top_url()

    def get_top_url(self):
        return self.driver.current_url

    def can_get_details(self):
        element_id = 'LnkV0300_001Top'
        if self.scraping_manager.is_findable_element('ID', element_id):
            self.driver.find_element_by_id(element_id).click()
            return True
        return False

    def can_get_point(self):
        element_id = 'LnkV0800_002Top'
        if self.scraping_manager.is_findable_element('ID', element_id):
            self.driver.find_element_by_id(element_id).click()
            return True
        return False

    def get_details(self):
        details = {}
        card_select_element_id = 'DdlCardNO'
        back_btn_element_id = 'BtnReSelect'
        card_count = len(
            self.driver.find_element_by_id(card_select_element_id).find_elements_by_tag_name('option')
            )
        for card_no in range(card_count):
            one_details = {}
            one_details['card_name'] = self.select_card(card_select_element_id, card_no)
            if self.can_get_unconfirmed_detail():
                self.get_unconfirmed_detail(back_btn_element_id)
            if self.can_get_confirmed_detail():
                self.get_confirmed_details(back_btn_element_id)
            details[card_no] = one_details
        self.driver.get(self.top_url)
        return details

    def select_card(self,  card_select_element_id, card_no):
        card_select = Select(self.driver.find_element_by_id(card_select_element_id))
        card_select.select_by_index(card_no)
        return card_select.first_selected_option.text

    def can_get_unconfirmed_detail(self):
        element_id = 'LnkYotei'
        if self.scraping_manager.is_findable_element('ID', element_id):
            self.driver.find_element_by_id('LnkYotei').click()
            return True
        return False
    
    def can_get_confirmed_detail(self):
        element_id = 'LnkClaimYm1'
        if self.scraping_manager.is_findable_element('ID', element_id):
            return True
        return False

    def get_unconfirmed_detail(self, back_btn_element_id):
        self.parse_detail_table()
        self.driver.find_element_by_id(back_btn_element_id).click()

    def get_confirmed_details(self, back_btn_element_id):
        element_id = 'LnkClaimYm'
        confirmed_detail_count = len(
            self.driver.find_elements_by_xpath(f'//*[contains(@id, \'{element_id}\')]')
            )
        for i in range(1, confirmed_detail_count + 1):
            self.driver.find_element_by_id(element_id + str(i)).click()
            self.get_one_payment()
            self.parse_detail_table()
            self.get_pdf()
            sleep(1) # 後で削除
            if i != confirmed_detail_count + 1:
                self.driver.find_element_by_id(back_btn_element_id).click()
    
    def get_one_payment(self):
        pass

    def parse_detail_table(self):
        pass

    def get_pdf(self):
        pass

    def get_point(self):
        point = {}
        return point

    def main(self):
        try:
            info = {}
            # current url is self.top_url
            if self.can_get_details():
                details = self.get_details()
            # current url is self.top_url
            if self.can_get_point():
                point = self.get_point()
            # self.pdf結合処理
            info.update(details = details, point = point)
            self.scraping_manager.current_process = const.CURRENT_PROCESS['COMPLETED']
            return  info
        except Exception as e:
            print('=== Error occurred  ===')
            print('type:' + str(type(e)))
            print('args:' + str(e.args))
            print('e:' + str(e))
            self.scraping_manager.current_process = const.CURRENT_PROCESS['QUIT']
