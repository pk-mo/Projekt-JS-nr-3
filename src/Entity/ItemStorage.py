import random


class ItemStorage:
    """The item storage. Used to store items in the machine."""

    def __init__(self):
        self.prices = self.__get_initial_prices_dictionary()
        self.items = self.__get_initial_items_dictionary()

    def __get_initial_prices_dictionary(self, min_key: int = 30, max_key: int = 50) -> {int, int}:
        """Gets the initial dictionary for storing item prices."""
        return {key: random.randint(10, 1000) for key in range(min_key, max_key + 1)}

    def __get_initial_items_dictionary(self, min_key: int = 30, max_key: int = 50, default_item_amount: int = 5):
        """Gets the initial dictionary for storing item amounts."""
        return {key: default_item_amount for key in range(min_key, max_key + 1)}

    def take_item(self, item_id: int) -> bool:
        """Takes the item from the item storage."""
        if self.items[item_id] < 1:
            return False
        self.items[item_id] -= 1
        return True

    def get_item_price(self, item_id: int) -> int:
        """Gets the item price."""
        return self.prices[item_id]

    def get_items_amount(self, item_id: int) -> int:
        """Gets the item amount."""
        return self.items[item_id]
