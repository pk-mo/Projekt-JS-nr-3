from copy import deepcopy

from . import Coin
from ..Utils import CoinUtils


class CoinStorage:
    """The coin storage. Used to store coins in the machine."""

    def __init__(self):
        """CoinStorage constructor,"""
        self.coins = self.__get_initial_coins_dictionary()

    def __get_initial_coins_dictionary(self) -> {int, list}:
        """Gets the initial dictionary for storing coins."""
        return {key: [] for key in Coin.get_valid_coin_values()}

    def insert(self, coins: [Coin.Coin]) -> None:
        """Inserts the coin into the coin storage."""
        for coin in coins:
            self.coins[coin.get_value()].append(coin)

    def get_amount(self) -> int:
        """Gets the amount of money in coin storage."""
        return sum(coin.get_amount() for coin in self.coins)

    def withdraw(self, amount: int) -> [Coin.Coin]:
        """Withdraws the amount of money from coin storage."""
        coin_types_sorted = sorted(Coin.get_valid_coin_values(), reverse=True)
        coins = deepcopy(self.coins)
        coins_to_withdraw = CoinUtils.give_change(coins, coin_types_sorted, amount)
        self.coins = coins
        return coins_to_withdraw
