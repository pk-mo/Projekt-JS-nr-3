import dearpygui.dearpygui as dpg

from machine import get_transaction, get_machine
from src.Exception import *
from src.Presentation import InsertCoins, Messages
from src.Utils import PresentationUtils

select_product_input = ''


def input_callback(value: str):
    """Callback handling selection of product."""
    global select_product_input
    select_product_input += value
    Messages.add_selected_product_message("Selected product: " + select_product_input)
    buy()


def buy():
    """Handles the purchase of product."""
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
    """Aborts the transaction."""
    InsertCoins.withdraw()
    clear_selected_product()
    __clear_messages()
    Messages.add_error_message('Transaction aborted')


def __clear_messages():
    """Clears the product and alert messages."""
    Messages.reset_product_price_message()
    Messages.reset_product_amount_message()
    Messages.reset_error_message()
    Messages.reset_success_message()


def clear_selected_product():
    """Clears the selected product."""
    global select_product_input
    select_product_input = ''
    Messages.reset_selected_product_message()


def render():
    """Renders interface of selecting product."""
    with dpg.window(label="Select products", width=500, height=500, pos=[0, 0], no_move=True, no_collapse=True,
                    no_close=True, no_resize=True):
        Messages.render_product_messages()
        Messages.render_alert_messages()
        dpg.add_spacer(height=20)
        __render_product_input()


def __render_product_input():
    """Renders input buttons for product selection and aborting the transaction."""
    with dpg.group(horizontal=True, horizontal_spacing=10):
        PresentationUtils.render_button('1', lambda _: input_callback('1'))
        PresentationUtils.render_button('2', lambda _: input_callback('2'))
        PresentationUtils.render_button('3', lambda _: input_callback('3'))
    with dpg.group(horizontal=True, horizontal_spacing=10):
        PresentationUtils.render_button('4', lambda _: input_callback('4'))
        PresentationUtils.render_button('5', lambda _: input_callback('5'))
        PresentationUtils.render_button('6', lambda _: input_callback('6'))
    with dpg.group(horizontal=True, horizontal_spacing=10):
        PresentationUtils.render_button('7', lambda _: input_callback('7'))
        PresentationUtils.render_button('8', lambda _: input_callback('8'))
        PresentationUtils.render_button('9', lambda _: input_callback('9'))
    with dpg.group(horizontal=True, horizontal_spacing=10):
        PresentationUtils.render_button('0', lambda _: input_callback('0'))
        PresentationUtils.render_button('Abort', abort, width=90, height=60)
