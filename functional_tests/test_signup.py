from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestSignUp(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_view_signup_page_title(self):
        # Paul visits the signup page from the home page or by typing it in the url
        self.browser.get(self.live_server_url + '/signup/')
        self.assertIn(self.browser.title, 'Sign Up')

    def test_new_viewer_can_create_account(self):
        # Paul now wants to create an account :
        self.browser.get(self.live_server_url + '/signup/')

        # He must first type his username
        username_input_box = self.browser.find_element_by_id('id_input_box_username')
        self.assertEqual(
                username_input_box.get_attribute('placeholder'),
                "Entrez votre nom d'utilisateur"
            )
        # He enters his username :
        username_input.send_keys('Paul')
        
        # He then has to type in his email adress:
        email_input_box = self.browser.find_element_by_id('id_input_box_email')
        self.assertEqual(
            email_input_box.get_attribute('placeholder'),
            "Entrez votre adresse email"
        )
        email_input.send_keys('paulypaul@mail.com')

        # Last steps of the signup, typing in a password and confirming it
        passwd_input_box = self.browser.find_element_by_id('id_input_passwd')
        self.assertEqual(
            passwd_input_box.get_attribute('placeholder'),
            "Entrez un mot de passe"
        )
        passwd_input.send_keys('password123')

        # He finally has to confirm it :
        passwd_confirmation_input_box = self.browser.find_element_by_id('id_passwd_confirmation')
        self.assertEqual(
            passwd_confirmation_input_box.get_attribute('placeholder'),
            "Confirmez votre mot de passe"
        )
        passwd_confirmation_input_box.send_keys('password123')

        passwd_confirmation_input_box.send_keys(Keys.Enter)

        self.assertRedirects(response, 
                            self.live_server_url + '/login/', 
                            status_code=302, 
                            target_status_code=200, 
                            msg_prefix='', 
                            fetch_redirect_response=True
        )