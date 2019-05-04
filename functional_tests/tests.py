import time
import unittest

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get(self.live_server_url)
        self.assertIn('To-do', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-do list', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), '할일을 입력하세요')

        # input 1 item
        inputbox.send_keys('시장에서 미역 사기')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(5)

        # check 1 item
        self.check_for_row_in_list_table('1: 시장에서 미역 사기')

        # input 1 more item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('공작깃털을 이용해서 그물 만들기')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(5)

        # two items in the list
        self.check_for_row_in_list_table('1: 시장에서 미역 사기')
        self.check_for_row_in_list_table('2: 공작깃털을 이용해서 그물 만들기')

        self.fail('테스트 종료')

