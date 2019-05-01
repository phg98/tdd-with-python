from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from .views import home_page


class HomePageTest(TestCase):
    def test_root_url(self):
        fount = resolve('/')
        self.assertEqual(fount.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!Doctype'))
        self.assertIn('<title>일정관리</title>', html)
        self.assertTrue(html.endswith('</html>\n'))
