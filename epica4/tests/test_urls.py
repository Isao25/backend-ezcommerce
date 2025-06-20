from django.urls import resolve, reverse
from django.test import SimpleTestCase
from epica4 import views

class TestUrls(SimpleTestCase):
    def test_index_url_resolves(self):
        url = reverse('epica4:index')  # Usar el namespace de la app
        self.assertEqual(resolve(url).func, views.index)
