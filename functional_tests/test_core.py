from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestCore(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_view_index_page_title(self):
        # Paul goes to the home page and notices the title
        self.browser.get(self.live_server_url)

        self.assertIn(self.browser.title, 'Pur Beurre')

        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn(header_text, 'Pas du h1 mais presque')