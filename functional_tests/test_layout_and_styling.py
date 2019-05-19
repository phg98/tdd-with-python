from functional_tests.base import FunctionalTest
import os
import time
import unittest
from unittest import skip

from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class LayoutAndStylingTest(FunctionalTest):
    def test_layout_and_styling(self):
        sleeptime = self.sleeptime

        # Edith visits home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # Input box at the center
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            245,
            delta=10
        )

        # Start new list and check input box is in the center
        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(sleeptime)
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            245,
            delta=10
        )
