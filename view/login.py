import sys
import os

from selenium.webdriver.support.ui import WebDriverWait

sys.path.append(os.pardir)
import common
import const


class Login:
    def __init__(self, scraping_manager, args):
        self.scraping_manager = scraping_manager
        self.driver = scraping_manager.driver
        self.args = args
        self.wait = WebDriverWait(scraping_manager.driver, 5)

    def go_to_login(self):
        self.driver.get('https://viewsnet.jp/default.htm')

    def login(self, login_id, login_password):
        self.driver.find_element_by_id('id').send_keys(login_id)
        self.driver.find_element_by_id('pass').send_keys(login_password)
        self.driver.find_element_by_xpath('//*[@id=\"input_form\"]/form/p/input').click()

    # TODO: エラー文言が表示されている場合やメンテナンスだった場合
    def check_logged_in(self):
        content_text = self.driver.find_element_by_xpath('/html/body').text
        if "前回ログイン" in content_text:
            print('login succeed!')
        elif 'サービスIDまたはパスワードが間違っています。ご確認の上、再度入力してください。' in content_text:
            raise Exception('login failed!')

    def main(self):
        try:
            args = common.convert_json_to_dict(self.args)
            login_id = args['login_id']
            login_password = args['login_password']
            self.go_to_login()
            self.login(login_id, login_password)
            self.check_logged_in()
            self.scraping_manager.current_process = const.CURRENT_PROCESS['GET_INFO']
        except Exception as e:
            print('=== Error occurred  ===')
            print('type:' + str(type(e)))
            print('args:' + str(e.args))
            print('e:' + str(e))
            self.scraping_manager.current_process = const.CURRENT_PROCESS['QUIT']
