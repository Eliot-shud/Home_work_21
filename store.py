from base_storage import BaseStorage


class Store(BaseStorage):

    def __init__(self, items, capacity=100):
        super().__init__(items, capacity)