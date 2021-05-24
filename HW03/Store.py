class Store:
    __storeName = "MyShop"
    __storage = []

    def __init__(self, storeName):
        if len(str(storeName)) > 0:
            self.__storeName = str(storeName)

    def add_product(self, product, number_of_products=1):
        if number_of_products <= 0:
            return
        for item in self.__storage:
            if item[0].get_id() == product.get_id() and item[0].get_price() == product.get_price():
                item[1] += number_of_products
                return
        product_unit = [product, number_of_products]
        self.__storage.append(product_unit)

    def __get_all_product(self):
        result = []
        for item in self.__storage:
            result.append(item[0])
        return result

    def __get_products_by_id(self, id):
        for item in self.__get_all_product():
            if item.get_Id() == id:
                return item

    def __get_products_by_price(self, price):
        result = []
        for item in self.__get_all_product():
            if item.get_price() == price:
                result.append(item)
        return result

    def __get_products_by_down_price(self, price):
        result = []
        for item in self.__get_all_product():
            if item.get_price() <= price:
                result.append(item)
        return result

    def __get_products_by_up_price(self, price):
        result = []
        for item in self.__get_all_product():
            if item[0].get_price() >= price:
                result.append(item)
        return result

    def print_all_products(self):
        for item in self.__storage:
            print(item[0], f"\nКоличество {item[1]}\n{'-' * 10}")

    def print_products_total_price(self):
        for item in self.__storage:
            print(item[0], f"\nКоличество {item[1]}\nПолная стоимость {item[1] * item[0].get_price()}$\n{'-' * 10}")

    def print_product_by_name_and_low_price(self, name, price):
        for item in self.__get_products_by_down_price(price):
            if item.get_product_name().lower() == str(name).lower():
                print(item, f"\n{'-' * 10}")

    def print_product_by_name(self, name):
        for item in self.__get_all_product():
            if item.get_product_name().lower() == str(name).lower():
                print(item, f"\n{'-' * 10}")
