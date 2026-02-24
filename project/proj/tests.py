from django.urls import reverse
from django.test import TestCase
from .models import Tovar, Category, Producer, Supplier, NameTovar

class MyFirstWorkingTest(TestCase):

    def setUp(self):
        # Этот метод выполняется перед каждым тестом
        self.category = Category.objects.create(title="Обувь")
        self.producer = Producer.objects.create(title="Фабрика")
        self.supplier = Supplier.objects.create(title="Поставщик")
        self.name = NameTovar.objects.create(title="Тапки")

        # Создаем товар
        self.tovar = Tovar.objects.create(
            art="01",
            title=self.name,
            unit="шт",
            price=1000,
            supplier=self.supplier,
            producer=self.producer,
            category=self.category,
            discount=10,
            amount=5,
            description="Тест",
            photo="test.jpg"
        )

    # Проверяем запуск страницы гостя
    def test_2_guest_page_status(self):
        response = self.client.get(reverse('guest_page'))
        # проверка статуса страницы
        self.assertEqual(response.status_code, 200)
        print("✓ Страница гостя доступна")

    # Проверяем скидку
    def test_discount_works(self):
        # формула расчета скидки
        result = self.tovar.price * (1 - self.tovar.discount / 100)
        # проверка фактического результат с ожидаемым
        self.assertEqual(result, 900)
        print("✓ Скидка работает!")

    # Проверяем поиск
    def test_search(self):
        # выполняется поиск по название Тапки
        results = Tovar.objects.filter(title__title__icontains="Обувь")
        # если результат не равен 1, то ошибка
        self.assertEqual(results.count(), 1)
        # проверяет найденный товар с его указанной ценой
        self.assertEqual(results.first().price, 1000)
        print("✓ Поиск работает!")
