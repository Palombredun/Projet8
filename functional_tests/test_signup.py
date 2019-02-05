from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class CreationUserTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_cas_acces_signup_page(self):
		# Georges wants to signup to the website in order to
		# save the products he wants to change
		self.browser.get(self.live_server_url)

		#He notices the web title and header that mentions the website name
		self.assertIn('Pur Beurre', self.browser.title)
		self.fail("End of test")