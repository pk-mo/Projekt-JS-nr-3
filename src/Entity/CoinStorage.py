from copy import deepcopy
from . import Coin
from ..Exception import InvalidCoinValueException


class CoinStorage:
    def __init__(self):
        self.coins = {key: [] for key in Coin.get_valid_coin_values()}

    def insert(self, coins: [Coin]) -> None:
        for coin in coins:
            self.coins[coin.get_value()].append(coin)

    def get_amount(self) -> int:
        return sum(coin.get_amount() for coin in self.coins)

    def withdraw(self, amount: int) -> [Coin]:
        coin_types_sorted = sorted(Coin.get_valid_coin_values(), reverse=True)
        coins = deepcopy(self.coins)
        coins_to_withdraw = []

        for coin_type in coin_types_sorted:
            while amount >= coin_type:
                coin = self.__withdraw_coin(coins, coin_type)
                if not coin:
                    break
                coins_to_withdraw.append(coin)
                amount -= coin_type

        if amount > 0:
            return None

        self.coins = coins
        return coins_to_withdraw

    def __withdraw_coin(self, coins: [Coin], amount: int):
        if amount not in Coin.get_valid_coin_values():
            raise InvalidCoinValueException()
        if len(coins[amount]) < 1:
            return None
        return coins[amount].pop()
