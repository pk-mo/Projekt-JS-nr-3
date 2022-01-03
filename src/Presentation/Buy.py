import dearpygui.dearpygui as dpg

from machine import get_transaction
from src.Exception import *
from src.Presentation import SelectProduct, InsertCoins, Products


def buy_callback():
    transaction = get_transaction()
    try:
        dpg.set_value("error_message", '')
        dpg.set_value("success_message", '')
        if len(SelectProduct.select_product_input):
            transaction.select_item(int(SelectProduct.select_product_input))
            change = transaction.buy()
            if change:
                InsertCoins.return_change(change)
            SelectProduct.clear_callback()
            Products.refresh_table()
            dpg.set_value("success_message",
                          "Successful purchase of item with id " + str(transaction.get_selected_item_id()))
    except OnlyCalculatedAmountException.OnlyCalculatedAmountException as err:
        InsertCoins.withdraw()
        dpg.set_value("error_message", err.__str__())
    except Exception as err:
        dpg.set_value("error_message", err.__str__())


def abort_callback():
    InsertCoins.withdraw()
    SelectProduct.clear_callback()
    dpg.set_value("success_message", '')
    dpg.set_value("error_message", "Transaction aborted")


def render():
    with dpg.window(label="Buy", width=500, height=400, pos=[1000, 0], no_move=True, no_collapse=True,
                    no_close=True, no_resize=True):
        dpg.add_button(label="Buy", callback=buy_callback, width=500, height=100)
        dpg.add_button(label="Abort", callback=abort_callback, width=500, height=100)
        dpg.add_text(color=[0, 255, 0], tag="success_message")
        dpg.add_text(color=[255, 0, 0], tag="error_message")
