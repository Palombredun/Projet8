from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from django.core.exceptions import ValidationError

from signup.models import User
from signup.views import signup

class SignUpTest(TestCase):
    def test_uses_signup_page(self):
        found = resolve('/signup/')
        self.assertEqual(found.func, signup)

    def test_signup_returns_correct_html(self):
        request = HttpRequest()
        response = signup(request)
        self.assertIn(b'<title>Pur Beurre</title>', response.content)