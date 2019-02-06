from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase): 
    def setUp(self): 
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self): #
        self.browser.quit()

    def test_can_access_home_page(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get("http://purebutter.herokuapp.com/")

        # She notices the page title and header mention to-do lists
        self.assertIn('Pur Beurre', self.browser.title)

        ## TO DO later : tester redirections du header