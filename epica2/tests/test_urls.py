from django.urls import resolve, reverse
from django.test import SimpleTestCase
from epica2 import views

class TestUrls(SimpleTestCase):
    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, views.index)
