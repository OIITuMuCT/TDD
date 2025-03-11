from unittest import skip
from selenium.common.exceptions import WebDriverException
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import unittest
import time
import os


MAX_WAIT = 10


# service = Service(executable_path="/snap/bin/geckodriver")
service = Service(
    executable_path="/home/neko/Documents/Projects/TDD/chromedriver-linux64/chromedriver"
)
browser = webdriver.Chrome(service=service)

class FunctionalTest(StaticLiveServerTestCase):
    """
    Функциональный тест
    """
    def setUp(self):
        """Установка"""
        self.browser = webdriver.Chrome(service=service)
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        """ демонтаж """
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        """ ожидать строку в таблице списка """
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, "id_list_table")
                rows = table.find_elements(By.TAG_NAME, 'tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def wait_for(self, fn):
        """ожидать"""
        start_time = time.time()
        while True:
            try:
                return fn()

            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def get_item_input_box(self):
        """ получить поле ввода для элемента """
        return self.browser.find_element(By.ID, 'id_text')

# if __name__ == '__main__':
#     unittest.main(warnings='ignore')