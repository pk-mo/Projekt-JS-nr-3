import dearpygui.dearpygui as dpg

from machine import get_transaction, get_machine
from src.Exception import *
from src.Presentation import InsertCoins, Messages
from src.Utils import PresentationUtils

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
    Messages.add_selected_product_message("Selected product: " + select_product_input)
    buy()


def buy():
    __clear_messages()
    machine = get_machine()
    transaction = get_transaction()
    if len(select_product_input) == 0:
        return
    try:
        transaction.select_item(int(select_product_input))
        Messages.add_product_price_message(
            f'Price: {machine.get_product_price(transaction.get_selected_item_id()) / 100}zl')
        Messages.add_product_amount_message(
            f'Amount in machine: {machine.get_product_amount(transaction.get_selected_item_id())}')
        change = transaction.buy()
        InsertCoins.return_change(change)
        clear_selected_product()
        __clear_messages()
        Messages.add_success_message("Successful purchase of item with id " + str(transaction.get_selected_item_id()))
    except OnlyCalculatedAmountException.OnlyCalculatedAmountException as err:
        InsertCoins.withdraw()
        Messages.add_error_message(err.__str__())
    except Exception as err:
        Messages.add_error_message(err.__str__())


def abort():
    InsertCoins.withdraw()
    clear_selected_product()
    __clear_messages()
    Messages.add_error_message('Transaction aborted')


def __clear_messages():
    Messages.reset_product_price_message()
    Messages.reset_product_amount_message()
    Messages.reset_error_message()
    Messages.reset_success_message()


def clear_selected_product():
    global select_product_input
    select_product_input = ''
    Messages.reset_selected_product_message()


def render():
    with dpg.window(label="Select products", width=500, height=500, pos=[0, 0], no_move=True, no_collapse=True,
                    no_close=True, no_resize=True):
        Messages.render_product_messages()
        Messages.render_alert_messages()
        dpg.add_spacer(height=20)
        __render_product_input()


def __render_product_input():
    with dpg.group(horizontal=True, horizontal_spacing=10):
        PresentationUtils.render_button('1', input_1_callback)
        PresentationUtils.render_button('2', input_2_callback)
        PresentationUtils.render_button('3', input_3_callback)
    with dpg.group(horizontal=True, horizontal_spacing=10):
        PresentationUtils.render_button('4', input_4_callback)
        PresentationUtils.render_button('5', input_5_callback)
        PresentationUtils.render_button('6', input_6_callback)
    with dpg.group(horizontal=True, horizontal_spacing=10):
        PresentationUtils.render_button('7', input_7_callback)
        PresentationUtils.render_button('8', input_8_callback)
        PresentationUtils.render_button('9', input_9_callback)
    with dpg.group(horizontal=True, horizontal_spacing=10):
        PresentationUtils.render_button('0', input_0_callback)
        PresentationUtils.render_button('Abort', abort, width=90, height=60)
