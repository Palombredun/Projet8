from django.test import TestCase

class Index(TestCase):
    def test_uses_index_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'core/index.html')