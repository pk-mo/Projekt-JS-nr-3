import dearpygui.dearpygui as dpg

from src.Presentation.Handler import handle

dpg.create_context()
dpg.create_viewport(width=1500, height=700, resizable=False)
dpg.setup_dearpygui()

handle()

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
