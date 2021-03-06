from functional_tests.base import FunctionalTest
#import os
import time
#import unittest

#from django.test import LiveServerTestCase
#from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(FunctionalTest):
    def test_can_start_a_list_and_retrieve_it_later(self):
        sleeptime = self.sleeptime

        self.browser.get(self.live_server_url)
        self.assertIn('To-do', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('작업 목록 시작', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), '할일을 입력하세요')

        # Enter input redirects to new URL and add item to list
        inputbox.send_keys('시장에서 미역 사기')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(sleeptime)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: 시장에서 미역 사기')

        # input 1 more item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('공작깃털을 이용해서 그물 만들기')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(sleeptime)

        # two items in the list
        self.check_for_row_in_list_table('1: 시장에서 미역 사기')
        self.check_for_row_in_list_table('2: 공작깃털을 이용해서 그물 만들기')

        # new user francis connects

        ## use new browser sesstoin
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis connects to home page.
        # Edith's list should NOT be shown
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('미역', page_text)
        self.assertNotIn('공작깃털', page_text)

        # Francis enter new item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('우유 사기')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(sleeptime)

        # Francis gets new URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Check edith's item is NOT on the list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('공작깃털', page_text)
        self.assertIn('우유', page_text)
