import dearpygui.dearpygui as dpg

from machine import get_transaction
from src.Entity.Coin import *
from . import SelectProduct


def get_inserted_coins_to_text(coins: [Coin]):
    text = ''
    for coin in coins:
        if len(text) > 0:
            text += ", "
        text += f'{coin.get_value() / 100}zl'
    return text


def input_500_callback(): input_callback(Coin(500))


def input_200_callback(): input_callback(Coin(200))


def input_100_callback(): input_callback(Coin(100))


def input_50_callback(): input_callback(Coin(50))


def input_20_callback(): input_callback(Coin(20))


def input_10_callback(): input_callback(Coin(10))


def input_5_callback(): input_callback(Coin(5))


def input_2_callback(): input_callback(Coin(2))


def input_1_callback(): input_callback(Coin(1))


def input_callback(coin: Coin):
    transaction = get_transaction()
    transaction.insert_coin(coin)
    dpg.set_value('inserted_coins_text', f'Inserted money: {transaction.get_inserted_money_amount() / 100} zl')
    SelectProduct.buy()

def withdraw():
    dpg.set_value("withdrawn_coins", '')
    transaction = get_transaction()
    coins = transaction.withdraw_inserted_coins()
    dpg.set_value('inserted_coins_text', 'Insert coins')
    if coins:
        dpg.set_value("withdrawn_coins", f'Returned coins: {get_inserted_coins_to_text(coins)}')


def return_change(change: [Coin]):
    dpg.set_value('inserted_coins_text', 'Insert coins')
    if change:
        dpg.set_value("withdrawn_coins", f'Returned change: {get_inserted_coins_to_text(change)}')
    else:
        dpg.set_value("withdrawn_coins", '')

def render():
    with dpg.window(label="Insert coins", width=500, height=500, pos=[500, 0], no_move=True, no_collapse=True,
                    no_close=True, no_resize=True):
        dpg.add_text("Insert coins", tag="inserted_coins_text")
        dpg.add_text(tag="withdrawn_coins")
        dpg.add_spacer(height=20)
        with dpg.group(horizontal=True, horizontal_spacing=10):
            dpg.add_button(label='5zl', callback=input_500_callback, width=40, height=60)
            dpg.add_button(label='2zl', callback=input_200_callback, width=40, height=60)
            dpg.add_button(label='1zl', callback=input_100_callback, width=40, height=60)
        with dpg.group(horizontal=True, horizontal_spacing=10):
            dpg.add_button(label='50gr', callback=input_50_callback, width=40, height=60)
            dpg.add_button(label='20gr', callback=input_20_callback, width=40, height=60)
            dpg.add_button(label='10gr', callback=input_10_callback, width=40, height=60)
        with dpg.group(horizontal=True, horizontal_spacing=10):
            dpg.add_button(label='5gr', callback=input_5_callback, width=40, height=60)
            dpg.add_button(label='2gr', callback=input_2_callback, width=40, height=60)
            dpg.add_button(label='1gr', callback=input_1_callback, width=40, height=60)
