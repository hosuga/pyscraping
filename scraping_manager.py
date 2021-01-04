import json
from time import sleep
from importlib import import_module
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import config
import const
from view.login import Login
#from view.authenticate import AUTHENTICATE
from view.get_info import GetInfo

class ScrapingManager:
    def __init__(self):
        self.driver = self.generate_driver()
        self.is_quit = False
        self.current_process = const.CURRENT_PROCESS['LOGIN']
    
    def generate_driver(self):
        options = Options()
        #options.add_argument('--headless')
        options.add_argument('--incognito')
        driver = webdriver.Chrome(config.CHROMEDRIVER_PATH, options=options)
        #ページが完全にロードされるまでまでの待機時間 最大10秒
        driver.set_page_load_timeout(10)
        #要素が見つかるまでの待機時間 最大10秒
        driver.implicitly_wait(15)
        #Javascript実行が終了するまでの待機時間 最大10秒
        driver.set_script_timeout(10)
        return driver
    
    def quit_driver(self):
        self.is_quit = True
    
    def is_findable_element(self, attribute, value):
        return self.driver.find_elements(getattr(By, attribute), value)
    
    # 仮の呼出メソッド
    # fromパッケージを変更して、各サイトで利用する
    def main(self):
        while True:
            if self.current_process == const.CURRENT_PROCESS['LOGIN']:
                print('=== Start login ===')
                args = input('{"login_id": "xxxxx", "login_password": "xxxxx"}: ')
                Login(self, args).main()
            elif self.current_process == const.CURRENT_PROCESS['AUTHENTICATE']:
                print('=== Start authenticate ===')
                args = input('{"answer": "xxxxx"}: ')
                # AUTHENTICATE(self, args).main()
            elif self.current_process == const.CURRENT_PROCESS['GET_INFO']:
                print('=== Start get_info ===')
                raw_result = GetInfo(self, args).main()
            elif self.current_process == const.CURRENT_PROCESS['COMPLETED']:
                print('=== Completed ===')
                encoded_result = json.dumps(raw_result)
                print(encoded_result)
                self.quit_driver()
            elif self.current_process == const.CURRENT_PROCESS['QUIT']:
                print('=== Quit ===')
                self.quit_driver()
            if self.is_quit:
                break
