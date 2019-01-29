from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from core.views import index

class IndexPageTest(TestCase):
    def test_root_url_resolves_to_index_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)
