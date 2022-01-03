import dearpygui.dearpygui as dpg

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


def clear_callback():
    global select_product_input
    select_product_input = ''
    dpg.set_value('selected_product_text', "Select product")


def render():
    with dpg.window(label="Select products", width=500, height=400, pos=[0, 0], no_move=True, no_collapse=True,
                    no_close=True, no_resize=True):
        dpg.add_text("Select product", tag="selected_product_text")
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
            dpg.add_button(label='Clear', callback=clear_callback, width=90, height=60)
