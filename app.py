import dearpygui.dearpygui as dpg

from src.Presentation.Handler import handle

if __name__ == '__main__':
    dpg.create_context()
    dpg.create_viewport(title='Projekt JS nr 3', width=1000, height=500, resizable=False)
    dpg.setup_dearpygui()

    handle()

    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
