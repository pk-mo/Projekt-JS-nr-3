import re
from unittest import mock

from src.Entity import Coin
from src.Presentation import InsertCoins, SelectProduct


def gui_mock():
    """Mocks the presentation layer."""
    return mock.patch('src.Presentation.Messages.dpg')


def assert_gui_message_rendered(message: str, gui) -> None:
    """Asserts, that a message appeared in the GUI."""
    message_call = filter(lambda call_args: call_args.args[1] == message,
                          gui.set_value.call_args_list)
    assert len(list(message_call)) > 0


def assert_gui_message_pattern_rendered(pattern: str, gui) -> None:
    """Asserts, that a message, matching the pattern, appeared in the GUI."""
    message_call = filter(
        lambda call_args: re.search(pattern, call_args.args[1]),
        gui.set_value.call_args_list)
    assert len(list(message_call)) > 0


def assert_gui_message_not_rendered(message: str, gui) -> None:
    """Asserts, that a message not appeared in the GUI."""
    message_call = filter(lambda call_args: call_args.args[1] == message,
                          gui.set_value.call_args_list)
    assert len(list(message_call)) == 0


def assert_gui_message_pattern_not_rendered(pattern: str, gui) -> None:
    """Asserts, that a message, matching the pattern, not appeared in the GUI."""
    message_call = filter(
        lambda call_args: re.search(pattern, call_args.args[1]),
        gui.set_value.call_args_list)
    assert len(list(message_call)) == 0


def buy_product(item_id: int, price: int):
    """Buys a product in the GUI."""
    for _ in range(price):
        InsertCoins.input_callback(Coin.Coin(1))
    SelectProduct.input_callback(str(item_id))
