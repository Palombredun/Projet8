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
        self.browser.get("http://purebutter.herokuapp.com/signup/")

        #He notices the web title and header that mentions the website name
        self.assertIn('Sign Up', self.browser.title)
        
        # He is proposed to enter his username :
        username = self.browser.find_elements_by_name('username')
        self.assertEqual(
            username.get_attribute('placeholder'),
            "Nom d'utilisateur")
        # He types in his name : 'Georges' :
        username.send_keys('Georges')

        # Then his email adresse:
        email = self.browser.find_elements_by_name('email')
        self.assertEqual(
            email.get_attribute('placeholder'),
            "Email")
        # He types in his email adress :
        email.send_keys('georgygeorges@email.com')

        # Finally, he has to enter a password to complete his signing up :
        password = self.browser.find_element_by_name('password')
        self.assertEqual(
            password.get_attribute('placeholder'),
            "Mot de passe")
        # He types in his password :
        password.send_keys('Georges123')