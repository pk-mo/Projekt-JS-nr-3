from src.Transaction import *


class Machine:
    def __init__(self):
        self.coin_storage = CoinStorage.CoinStorage()
        self.item_storage = ItemStorage.ItemStorage()
        self.transaction = None

    def start(self) -> Transaction:
        self.transaction = Transaction(self.coin_storage, self.item_storage)
        return self.transaction

    def get_product_data(self):
        return {item_id: {"price": self.item_storage.get_item_price(item_id),
                          "amount": self.item_storage.get_items_amount(item_id)} for item_id in self.item_storage.items}
