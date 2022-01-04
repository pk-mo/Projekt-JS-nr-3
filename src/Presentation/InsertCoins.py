import dearpygui.dearpygui as dpg

from machine import get_transaction
from src.Entity.Coin import *
from . import Messages
from . import SelectProduct
from ..Utils import CoinUtils, PresentationUtils


def input_callback(coin: Coin):
    """Callback handling insertion of coin into the machine."""
    transaction = get_transaction()
    transaction.insert_coin(coin)
    Messages.add_inserted_coins_message(f'Inserted money: {transaction.get_inserted_money_amount() / 100}zl')
    SelectProduct.buy()


def withdraw():
    """Withdraws coins inserted into the machine."""
    Messages.reset_withdrawn_coins_message()
    Messages.reset_inserted_coins_message()
    transaction = get_transaction()
    coins = transaction.withdraw_inserted_coins()
    if coins:
        Messages.add_withdrawn_coins_message(f'Returned coins: {CoinUtils.coins_to_string(coins)}')


def return_change(change: [Coin]):
    """Returns the change after product purchase."""
    Messages.reset_inserted_coins_message()
    if change:
        Messages.add_withdrawn_coins_message(f'Returned change: {CoinUtils.coins_to_string(change)}')
    else:
        Messages.reset_withdrawn_coins_message()


def render():
    """Renders interface of inserting coins"""
    with dpg.window(label="Insert coins", width=500, height=500, pos=[500, 0], no_move=True, no_collapse=True,
                    no_close=True, no_resize=True):
        Messages.render_coins_messages()
        dpg.add_spacer(height=20)
        __render_coins_input()


def __render_coins_input():
    """Renders input buttons for every possible coin."""
    with dpg.group(horizontal=True, horizontal_spacing=10):
        PresentationUtils.render_button('5zl', lambda _: input_callback(Coin(500)))
        PresentationUtils.render_button('2zl', lambda _: input_callback(Coin(200)))
        PresentationUtils.render_button('1zl', lambda _: input_callback(Coin(100)))
    with dpg.group(horizontal=True, horizontal_spacing=10):
        PresentationUtils.render_button('50gr', lambda _: input_callback(Coin(50)))
        PresentationUtils.render_button('20gr', lambda _: input_callback(Coin(20)))
        PresentationUtils.render_button('10gr', lambda _: input_callback(Coin(10)))
    with dpg.group(horizontal=True, horizontal_spacing=10):
        PresentationUtils.render_button('5gr', lambda _: input_callback(Coin(5)))
        PresentationUtils.render_button('2gr', lambda _: input_callback(Coin(2)))
        PresentationUtils.render_button('1gr', lambda _: input_callback(Coin(1)))
