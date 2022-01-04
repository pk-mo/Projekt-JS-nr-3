from ..Entity import Coin
from ..Exception import InvalidCoinValueException, NotEnoughCoinsToWithdrawException


def give_change(coins_source: [Coin.Coin], coin_types: [int], amount_of_change: int) -> [Coin.Coin]:
    coins_to_withdraw = []
    for coin_type in coin_types:
        while amount_of_change >= coin_type:
            coin = __get_coin_of_type(coins_source, coin_type)
            if not coin:
                break
            coins_to_withdraw.append(coin)
            amount_of_change -= coin_type
    if amount_of_change > 0:
        raise NotEnoughCoinsToWithdrawException.NotEnoughCoinsToWithdrawException()
    return coins_to_withdraw


def __get_coin_of_type(coins_source: [Coin.Coin], coin_type: int) -> Coin:
    if coin_type not in Coin.get_valid_coin_values():
        raise InvalidCoinValueException()
    if len(coins_source[coin_type]) < 1:
        return None
    return coins_source[coin_type].pop()


def coins_to_string(coins: [Coin]) -> str:
    text = ''
    for coin in coins:
        if len(text) > 0:
            text += ", "
        text += f'{coin.get_value() / 100}zl'
    return text


__all__ = ['coins_to_string', 'give_change']
