class Product:
    __lastId = 0
    __id = 0
    __productName = "Неисзвестно"
    __manufacturer = "Неисзвестно"
    __UPC = 0
    __price = 0.0
    __shelfLife = 0
    __amount = 0

    def __init__(self, product_name, manufacturer, upc, price, shelf_life=1):
        Product.__lastId += 1
        self.__id = self.__lastId
        self.set_product_name(product_name)
        self.set_manfacturer(manufacturer)
        self.set_upc(self.__id+1000)
        self.set_price(price)
        self.set_shelf_life(shelf_life)

    def __del__(self):
        Product.__id -= 1

    def __str__(self):
        info = []
        info.append(f"ID продукта {self.get_id()}")
        info.append(f"Имя продукта {self.get_product_name()}")
        info.append(f"Производитель {self.get_manfacturer()}")
        info.append(f"Штрихкод {self.get_upc()}")
        info.append(f"Цена {self.get_price()}$")
        info.append(f"Гарантия {self.get_shelf_life()} дней")
        return "\n".join(info)

    # Getters
    def get_id(self):
        return self.__id

    def get_product_name(self):
        return self.__productName

    def get_manfacturer(self):
        return self.__manufacturer

    def get_upc(self):
        return self.__UPC

    def get_price(self):
        return self.__price / 100

    def get_shelf_life(self):
        return self.__shelfLife

    # Setters

    def set_product_name(self, product_name):
        if len(str(product_name)) > 0:
            self.__productName = str(product_name)

    def set_manfacturer(self, manufacturer):
        if len(str(manufacturer)) > 0:
            self.__manufacturer = str(manufacturer)

    def set_upc(self, upc):
        if upc > 0:
            self.__UPC = upc

    def set_price(self, price):
        if price > 0:
            self.__price = price * 100

    def set_shelf_life(self, shelf_life):
        if shelf_life > 0:
            self.__shelfLife = shelf_life
