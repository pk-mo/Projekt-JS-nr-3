import dearpygui.dearpygui as dpg

from machine import get_machine


def refresh_table():
    dpg.delete_item("product_table")
    __render_table()


def __render_table():
    machine = get_machine()
    product_data = machine.get_product_data()
    with dpg.table(label="Test", tag="product_table", parent="product_table_window", borders_innerH=True):
        dpg.add_table_column(label="ID")
        dpg.add_table_column(label="Price")
        dpg.add_table_column(label="Amount")
        for item_id in product_data.keys():
            with dpg.table_row():
                dpg.add_text("Product " + str(item_id))
                dpg.add_text(str(product_data[item_id]["price"] / 100) + "zl")
                dpg.add_text(product_data[item_id]["amount"])


def render():
    with dpg.window(label="Products in machine", width=1500, height=300, pos=[0, 400], no_move=True, no_collapse=True,
                    no_close=True, no_resize=True, tag="product_table_window"):
        __render_table()
