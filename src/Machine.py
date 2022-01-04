from src.Transaction import *


class Machine:
    """The machine class. Represents the whole machine."""

    def __init__(self):
        self.coin_storage = CoinStorage.CoinStorage()
        self.item_storage = ItemStorage.ItemStorage()
        self.transaction = None

    def start(self) -> Transaction:
        """Starts the transaction in the machine."""
        self.transaction = Transaction(self.coin_storage, self.item_storage)
        return self.transaction

    def get_product_price(self, item_id: int):
        """Gets the product price."""
        return self.item_storage.get_item_price(item_id)

    def get_product_amount(self, item_id: int):
        """Gets the product amount."""
        return self.item_storage.get_items_amount(item_id)
