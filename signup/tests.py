from django.test import TestCase
from django.urls import resolve

from signup.views import signup


class SignUpTest(TestCase):
    def test_uses_signup_page(self):
        found = resolve('/signup/')
        self.assertEqual(found.func, signup)