#!/usr/bin/env python3


# Создать класс Product: id, Наименование, UPC, Производитель, Цена, Срок хранения, Количество.
# Функции-члены реализуют запись и считывание полей (проверка корректности), вывод общей суммы продукта.
# Создать список объектов.
# Вывести:
#     a) список товаров для заданного наименования;
#     b) список товаров для заданного наименования, цена которых не превосходит заданную;


from Store import Store
from Product import Product

my_store = Store("My Store")

apple = Product("Apple 3", "Apple", 12, 300.00, 1825)
apple1 = Product("Apple 4", "Apple", 123, 400.00, 1825)
apple2 = Product("Apple 5", "Apple", 1234, 500.50, 1825)
# Разная цена
apple3 = Product("Apple 6", "Apple", 12345, 599.99, 1825)
apple4 = Product("Apple 6", "Apple", 12345, 499.99, 1825)
apple5 = Product("Apple 6", "Apple", 12345, 399.99, 1825)

apple6 = Product("Apple 7", "Apple", 12345, 1000, 1825)

my_store.add_product(apple, 1)
my_store.add_product(apple1, 2)
my_store.add_product(apple2, 3)
my_store.add_product(apple3, 4)
my_store.add_product(apple4, 5)
my_store.add_product(apple5, 6)
# 2 раза одинаковая цена и ID
my_store.add_product(apple6, 6)
my_store.add_product(apple6, 7)

print(f"{'*' * 10}Все товары{'*' * 10}")
my_store.print_all_products()
print(f"{'*' * 10}Полная стоимость товара{'*' * 10}")
my_store.print_products_total_price()
print(f"{'*' * 10}Поиск по наименованию товара{'*' * 10}")
my_store.print_product_by_name("Apple 6")
print(f"{'*' * 10}Поиск по наименованию товара и цене{'*' * 10}")
my_store.print_product_by_name_and_low_price("Apple 6", 500)
