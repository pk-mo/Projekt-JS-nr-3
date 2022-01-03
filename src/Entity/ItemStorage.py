import random


class ItemStorage:
    def __init__(self):
        self.prices = {key: random.randint(10, 1000) for key in range(30, 51)}
        self.items = {key: 5 for key in range(30, 51)}

    def add_item(self, item_id: int) -> None:
        self.items[item_id] += 1

    def take_item(self, item_id: int) -> bool:
        if self.items[item_id] < 1:
            return False
        self.items[item_id] -= 1
        return True

    def get_item_price(self, item_id: int) -> int:
        return self.prices[item_id]

    def get_items_amount(self, item_id: int) -> int:
        return self.items[item_id]
