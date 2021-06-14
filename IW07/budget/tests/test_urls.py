from django.test import SimpleTestCase
from django.urls import reverse, resolve
from budget.views import project_list, project_detail, ProjectCreateView


# класс - набор тестов
class TestUrls(SimpleTestCase):
    # тест 1:
    # главная страница со списком проектов
    # генерируется функцией project_list?
    def test_list_url_resolves(self):
        # в функцию reverse передается значение атрибута name,
        # указанное в urls.py
        url = reverse('list')
        # сравнение функции, используемой для обработки полученного url,
        # c функцией project_list
        self.assertEquals(resolve(url).func, project_list)

    # тест 2:
    # страница добавления проекта
    # генерируется классом ProjectCreateView?
    def test_add_url_resolves(self):
        url = reverse('add')
        # сравнение класса, используемого для обработки полученного url,
        # c классом ProjectCreateView
        self.assertEquals(resolve(url).func.view_class, ProjectCreateView)

    # тест 3:
    # страница проекта с бюджетом и списком расходов
    # генерируется функцией project_detail?
    def test_detail_url_resolves(self):
        # подстановка произвольного аргумента 'some-slug'
        # в качестве названия проекта
        # (не обязательно существующего проекта -
        # этот тест проверяет, чтобы нужная фунция просто вызвалась,
        # результат функции будут проверять другие тесты)
        url = reverse('detail', args=['some-slug'])
        self.assertEquals(resolve(url).func, project_detail)
