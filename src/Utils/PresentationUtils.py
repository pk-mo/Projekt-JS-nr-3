from typing import Callable

import dearpygui.dearpygui as dpg


def render_button(label: str, callback: Callable, width: int = 40, height: int = 60) -> None:
    dpg.add_button(label=label, callback=callback, width=width, height=height)
