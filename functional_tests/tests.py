from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()


    def test_can_view_index_page_title(self):
        self.browser.get(self.live_server_url)
        self.assertIn(self.browser.title, 'Pur Beurre')

#if __name__ == '__main__':
#    unittest.main(warnings='ignore')