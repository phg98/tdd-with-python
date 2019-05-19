from functional_tests.base import FunctionalTest
#import time
from unittest import skip

#from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # Edith error input empty item
        # enter on empty
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

        # error message displayed
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, 'Empty item')

        # input other item and should be OK
        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')

        # empty item
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

        # error message on list page
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, 'Empty item')

        # input item and OK
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')