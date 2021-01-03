import sys
import os
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
sys.path.append(os.pardir)
import const

class GetInfo:
    def __init__(self, scraping_manager, args):
        self.scraping_manager = scraping_manager
        self.driver = scraping_manager.driver
        self.args = args
        self.wait = WebDriverWait(scraping_manager.driver, 5)
        self.info = {'payment_info':{}, 'confirmed_details_info':{}, 'unconfirmed_detail_info': {}, 'point_info': {}}
    
    def go_to_unconfirmed_detail(self):
        self.driver.find_element_by_id('LnkV0300_001Top').click()
        self.driver.find_element_by_id('LnkYotei').click()
    
    def get_one_payment_info(self):
        pass
    
    def get_unconfirmed_detail_info(self):
        pass

    def get_confirmed_details_info(self):
        detail_links_count = len(self.driver.find_element_by_id('vucV0300MonthList_list_month').find_elements_by_tag_name('a'))
        if detail_links_count == 0:
            return
        for i in range(detail_links_count):
            if i > 4:
                i +=1
            # ページが変わる毎に取得する必要あり
            detail_links = self.driver.find_element_by_id('vucV0300MonthList_list_month').find_elements_by_tag_name('a')
            link = detail_links[i].get_attribute("href")
            if not('javascript' in link):
                continue
            script = link.replace('javascript:', '')
            self.driver.execute_script(script)
    
    def main(self):
        try:
            self.go_to_unconfirmed_detail()
            self.get_unconfirmed_detail_info()
            self.get_confirmed_details_info()
            sleep(2)
            self.scraping_manager.current_process = const.CURRENT_PROCESS['COMPLETED']
        except Exception as e:
            print('=== Error occurred  ===')
            print('type:' + str(type(e)))
            print('args:' + str(e.args))
            print('e:' + str(e))
            self.scraping_manager.current_process = const.CURRENT_PROCESS['QUIT']
