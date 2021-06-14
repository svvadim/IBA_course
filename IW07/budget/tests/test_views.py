import json

from django.test import TestCase, Client
from django.urls import reverse


# класс - набор тестов
from budget.models import Project, Category, Expense


class TestViews(TestCase):
    # настройка, выполняемая перед запуском тестов:
    # подготовка эмулятора браузера (Client) и url-ов,
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('list')
        # будем искать проект с именем project1
        self.detail_url = reverse('detail', args=['project1'])
        # вставка проекта с именем project1 в БД
        self.project1 = Project.objects.create(
            name='project1',
            budget=10000
        )

    # тест 1:
    # главная страница со списком проектов
    # генерируется успешно (код 200) и
    # на основе шаблона budget/project-list.html?
    def test_project_list_GET(self):
        # обращение эмулятора браузера к странице со списком проектов
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'budget/project-list.html')

    # тест 2:
    # страница со списком расходов в проекте
    # генерируется успешно (код 200) и
    # на основе шаблона budget/project-detail.html?
    def test_project_detail_GET(self):
        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'budget/project-detail.html')

    # тест 3:
    # отправка на страницу со списком расходов в проекте
    # POST-запроса на добавление нового расхода заканчивается
    # переадресацией (код 302) на отображение страницы и
    # наличием нового расхода в БД?
    def test_project_detail_POST_add_expense(self):
        # создание в тестовом проекте категории для расходов
        Category.objects.create(project=self.project1, name='development')
        # отправка на страницу со списком расходов в проекте
        # POST-запроса на добавление нового расхода
        response = self.client.post(self.detail_url, {
            'title': 'expensel',
            'amount': 1000,
            'category': 'development'
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(
            self.project1.expenses.first().title,
            'expensel'
        )

    # тест 4:
    # отправка на страницу со списком расходов в проекте
    # POST-запроса БЕЗ ДАННЫХ заканчивается
    # переадресацией (код 302) на отображение страницы и
    # нулевым количеством расходов в БД?
    def test_project_detail_POST_no_data(self):
        response = self.client.post(self.detail_url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.project1.expenses.count(), 0)

    # тест 5:
    # отправка на страницу со списком расходов в проекте
    # DELETE-запроса с id расхода заканчивается
    # успешным выполнением без вывода данных (код 204) и
    # нулевым количеством расходов в БД?
    def test_project_detail_DELETE_deletes_expense(self):
        # создание категории через модель
        category1 = Category.objects.create(
            project=self.project1,
            name='development'
        )
        # создание расхода через модель
        Expense.objects.create(
            project=self.project1,
            title='expensel',
            amount=1000,
            category=category1
        )
        # отправка DELETE-запроса эмулятором браузера
        response = self.client.delete(
            self.detail_url,
            json.dumps({"id": 1})
        )
        # проверка результатов
        self.assertEquals(response.status_code, 204)
        self.assertEquals(self.project1.expenses.count(), 0)

    # тест 6:
    # отправка на страницу со списком расходов в проекте
    # DELETE-запроса БЕЗ id расхода заканчивается
    # сообщением об отсутствии страницы (код 404) и
    # сохранением одного расхода в БД?
    def test_project_detail_DELETE_no_id(self):
        category1 = Category.objects.create(
            project=self.project1,
            name='development'
        )
        Expense.objects.create(
            project=self.project1,
            title='expensel',
            amount=1000,
            category=category1
        )
        # отправка DELETE-запроса БЕЗ id расхода
        response = self.client.delete(self.detail_url)
        # проверка результатов
        self.assertEquals(response.status_code, 404)
        self.assertEquals(self.project1.expenses.count(), 1)
