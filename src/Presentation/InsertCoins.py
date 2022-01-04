import dearpygui.dearpygui as dpg

from machine import get_transaction
from src.Entity.Coin import *
from . import Messages
from . import SelectProduct
from ..Utils import CoinUtils, PresentationUtils


def input_callback(coin: Coin):
    transaction = get_transaction()
    transaction.insert_coin(coin)
    Messages.add_inserted_coins_message(f'Inserted money: {transaction.get_inserted_money_amount() / 100}zl')
    SelectProduct.buy()


def input_500_callback(): input_callback(Coin(500))


def input_200_callback(): input_callback(Coin(200))


def input_100_callback(): input_callback(Coin(100))


def input_50_callback(): input_callback(Coin(50))


def input_20_callback(): input_callback(Coin(20))


def input_10_callback(): input_callback(Coin(10))


def input_5_callback(): input_callback(Coin(5))


def input_2_callback(): input_callback(Coin(2))


def input_1_callback(): input_callback(Coin(1))


def withdraw():
    Messages.reset_withdrawn_coins_message()
    Messages.reset_inserted_coins_message()
    transaction = get_transaction()
    coins = transaction.withdraw_inserted_coins()
    if coins:
        Messages.add_withdrawn_coins_message(f'Returned coins: {CoinUtils.coins_to_string(coins)}')


def return_change(change: [Coin]):
    Messages.reset_inserted_coins_message()
    if change:
        Messages.add_withdrawn_coins_message(f'Returned change: {CoinUtils.coins_to_string(change)}')
    else:
        Messages.reset_withdrawn_coins_message()


def render():
    with dpg.window(label="Insert coins", width=500, height=500, pos=[500, 0], no_move=True, no_collapse=True,
                    no_close=True, no_resize=True):
        Messages.render_coins_messages()
        dpg.add_spacer(height=20)
        __render_coins_input()


def __render_coins_input():
    with dpg.group(horizontal=True, horizontal_spacing=10):
        PresentationUtils.render_button('5zl', input_500_callback)
        PresentationUtils.render_button('2zl', input_200_callback)
        PresentationUtils.render_button('1zl', input_100_callback)
    with dpg.group(horizontal=True, horizontal_spacing=10):
        PresentationUtils.render_button('50gr', input_50_callback)
        PresentationUtils.render_button('20gr', input_20_callback)
        PresentationUtils.render_button('10gr', input_10_callback)
    with dpg.group(horizontal=True, horizontal_spacing=10):
        PresentationUtils.render_button('5gr', input_5_callback)
        PresentationUtils.render_button('2gr', input_2_callback)
        PresentationUtils.render_button('1gr', input_1_callback)
