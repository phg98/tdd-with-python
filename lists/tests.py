from django.test import TestCase
from django.urls import resolve
from .views import home_page


class HomePageTest(TestCase):
    def test_root_url(self):
        fount = resolve('/')
        self.assertEqual(fount.func, home_page)


