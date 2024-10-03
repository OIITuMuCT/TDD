from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page

# Create your tests here.
# class SmokeTest(TestCase):
#     """тест на токсичность"""

#     def test_bad_maths(self):
#         """ тест: неправильные математические расчеты """
#         self.assertEqual(1 + 1, 3)

class HomePageTest(TestCase):
    """ Тест домашней страницы """
    def test_root_url_resolves_to_home_page_view(self):
        """ тест: коневой url преобразуется в представление домашней страницы """
        found = resolve('/')
        # resolve – это функция, которую Django использует внутренне для
        # преобразования URL-адреса и нахождения функций представления,
        # в соответствие которым они должны быть поставлены. Мы проверяем,
        # чтобы resolve, когда ее вызывают с «/», то есть корнем сайта,
        # нашла функцию под названием home_page.
        self.assertEqual(found.func, home_page)

    def test_home_returns_correct_html(self):
        """ тест: домашняя страница возвращает правильный html """
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode("utf8")
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
        
