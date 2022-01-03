import dearpygui.dearpygui as dpg

from machine import get_transaction, get_machine
from src.Exception import *
from src.Presentation import InsertCoins

select_product_input = ''


def input_1_callback(): input_callback('1')


def input_2_callback(): input_callback('2')


def input_3_callback(): input_callback('3')


def input_4_callback(): input_callback('4')


def input_5_callback(): input_callback('5')


def input_6_callback(): input_callback('6')


def input_7_callback(): input_callback('7')


def input_8_callback(): input_callback('8')


def input_9_callback(): input_callback('9')


def input_0_callback(): input_callback('0')


def input_callback(value: str):
    global select_product_input
    select_product_input += value
    dpg.set_value('selected_product_text', "Selected product: " + select_product_input)
    buy()


def __clear_messages():
    dpg.set_value("error_message", '')
    dpg.set_value("price_message", '')
    dpg.set_value("amount_message", '')
    dpg.set_value("success_message", '')


def buy():
    __clear_messages()
    machine = get_machine()
    transaction = get_transaction()
    if len(select_product_input) == 0:
        return
    try:
        transaction.select_item(int(select_product_input))
        dpg.set_value("price_message",
                      f'Price: {machine.get_product_price(transaction.get_selected_item_id()) / 100}zl')
        dpg.set_value("amount_message",
                      f'Amount in machine: {machine.get_product_amount(transaction.get_selected_item_id())}')
        change = transaction.buy()
        InsertCoins.return_change(change)
        clear()
        __clear_messages()
        dpg.set_value("success_message",
                      "Successful purchase of item with id " + str(transaction.get_selected_item_id()))
    except OnlyCalculatedAmountException.OnlyCalculatedAmountException as err:
        InsertCoins.withdraw()
        dpg.set_value("error_message", err.__str__())
    except Exception as err:
        dpg.set_value("error_message", err.__str__())


def abort():
    InsertCoins.withdraw()
    clear()
    __clear_messages()
    dpg.set_value("error_message", "Transaction aborted")


def clear():
    global select_product_input
    select_product_input = ''
    dpg.set_value('selected_product_text', "Select product")


def render():
    with dpg.window(label="Select products", width=500, height=500, pos=[0, 0], no_move=True, no_collapse=True,
                    no_close=True, no_resize=True):
        dpg.add_text("Select product", tag="selected_product_text")
        dpg.add_spacer(height=20)
        dpg.add_text(color=[0, 0, 255], tag="price_message")
        dpg.add_text(color=[0, 0, 255], tag="amount_message")
        dpg.add_text(color=[0, 255, 0], tag="success_message")
        dpg.add_text(color=[255, 0, 0], tag="error_message")
        dpg.add_spacer(height=20)
        with dpg.group(horizontal=True, horizontal_spacing=10):
            dpg.add_button(label='1', callback=input_1_callback, width=40, height=60)
            dpg.add_button(label='2', callback=input_2_callback, width=40, height=60)
            dpg.add_button(label='3', callback=input_3_callback, width=40, height=60)
        with dpg.group(horizontal=True, horizontal_spacing=10):
            dpg.add_button(label='4', callback=input_4_callback, width=40, height=60)
            dpg.add_button(label='5', callback=input_5_callback, width=40, height=60)
            dpg.add_button(label='6', callback=input_6_callback, width=40, height=60)
        with dpg.group(horizontal=True, horizontal_spacing=10):
            dpg.add_button(label='7', callback=input_7_callback, width=40, height=60)
            dpg.add_button(label='8', callback=input_8_callback, width=40, height=60)
            dpg.add_button(label='9', callback=input_9_callback, width=40, height=60)
        with dpg.group(horizontal=True, horizontal_spacing=10):
            dpg.add_button(label='0', callback=input_0_callback, width=40, height=60)
            dpg.add_button(label='Abort', callback=abort, width=90, height=60)
