from src.Entity import CoinStorage, ItemStorage, Coin
from src.Exception import InvalidItemIdException, TooSmallMoneyAmountException, NoItemInTheMachineException, \
    OnlyCalculatedAmountException


class Transaction:
    """Represents transaction, that can occur in the machine."""

    def __init__(self, coin_storage: CoinStorage, item_storage: ItemStorage.ItemStorage):
        self.coin_storage: CoinStorage.CoinStorage = coin_storage
        self.item_storage: ItemStorage.ItemStorage = item_storage
        self.inserted_coins = []
        self.selected_item = None

    def insert_coin(self, coin: Coin.Coin) -> None:
        """Inserts one coin to machine and current transaction."""
        self.inserted_coins.append(coin)

    def get_inserted_money_amount(self) -> int:
        """Returns amount of inserted money."""
        return sum(coin.get_value() for coin in self.inserted_coins)

    def withdraw_inserted_coins(self) -> [Coin.Coin]:
        coins_to_withdraw = self.inserted_coins
        self.inserted_coins = []
        return coins_to_withdraw

    def select_item(self, item_id: int) -> None:
        """Selects the item with specified id for purchase."""
        if item_id < 30 or item_id > 50:
            raise InvalidItemIdException.InvalidItemIdException()
        self.selected_item = item_id

    def get_selected_item_id(self) -> int:
        """Returns id of selected item."""
        return self.selected_item

    def buy(self) -> [Coin.Coin]:
        selected_item_price = self.item_storage.prices[self.get_selected_item_id()]
        selected_item_amount = self.item_storage.get_items_amount(self.get_selected_item_id())
        if self.get_inserted_money_amount() < selected_item_price:
            raise TooSmallMoneyAmountException.TooSmallMoneyAmountException(selected_item_amount > 0)
        if selected_item_amount < 1:
            raise NoItemInTheMachineException.NoItemInTheMachineException()

        change_amount = self.get_inserted_money_amount() - selected_item_price
        to_withdraw = []
        if change_amount > 0:
            change = self.coin_storage.withdraw(change_amount)
            if change is None:
                raise OnlyCalculatedAmountException.OnlyCalculatedAmountException()
            to_withdraw = change

        self.coin_storage.insert(self.inserted_coins)
        self.inserted_coins = []
        self.item_storage.take_item(self.get_selected_item_id())
        return to_withdraw
