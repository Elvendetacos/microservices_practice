import uuid


class Product_domain:
    def __init__(self, name: str, price: int, stock: int):
        self.id = str(uuid.uuid4())
        self.name = name
        self.price = price
        self.stock = stock

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_stock(self):
        return self.stock

    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price

    def set_stock(self, stock):
        self.stock = stock
