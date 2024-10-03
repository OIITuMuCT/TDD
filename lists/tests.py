from django.template.loader import render_to_string
from django.test import TestCase
from django.urls import resolve

from lists.views import home_page

# Create your tests here.
# class SmokeTest(TestCase):
#     """тест на токсичность"""

#     def test_bad_maths(self):
#         """ тест: неправильные математические расчеты """
#         self.assertEqual(1 + 1, 3)

class HomePageTest(TestCase):
    """ Тест домашней страницы """
    def test_uses_home_template(self):
        """ тест: используется домашний шаблон """
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
    
    # test 1
    # def test_root_url_resolves_to_home_page_view(self):
    #     """ тест: коневой url преобразуется в представление домашней страницы """
    #     found = resolve('/')
    #     self.assertEqual(found.func, home_page)

    # def test_home_returns_correct_html(self):
    #     """ тест: домашняя страница возвращает правильный html """
    #     response = self.client.get('/')
    #     # request = HttpRequest()
    #     # response = home_page(request)
    #     html = response.content.decode("utf8")
    #     self.assertTrue(html.startswith('<html>'))
    #     self.assertIn('<title>To-Do lists</title>', html)
    #     self.assertTrue(html.strip().endswith('</html>'))
        
    #     self.assertTemplateUsed(response, 'home.html')
