from base_storage import BaseStorage
from exceptions import TooManyDifferentProducts


class Shop(BaseStorage):

    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)

    def add(self, name, amount):
        # проверка, что в магазине хранится меньше 5 уникальных товаров
        if self.get_unique_items_count() > 5:
            raise TooManyDifferentProducts
        else:
            super().add(name, amount)