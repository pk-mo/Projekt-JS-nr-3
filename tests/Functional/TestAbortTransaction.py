import re
from unittest import mock

from machine import get_machine
from src.Entity import Coin
from src.Presentation import SelectProduct, InsertCoins
from tests.TestCase import TestCase


class TestAbortTransaction(TestCase):
    def test(self):
        with mock.patch('src.Presentation.SelectProduct.dpg'):
            with mock.patch('src.Presentation.InsertCoins.dpg') as coins_dpg:
                InsertCoins.input_callback(Coin.Coin(100))
                InsertCoins.input_callback(Coin.Coin(200))
                InsertCoins.input_callback(Coin.Coin(500))
                SelectProduct.abort()

                returned_coins_message = filter(
                    lambda call_args: call_args.args[1] == 'Returned coins: 1.0zl, 2.0zl, 5.0zl',
                    coins_dpg.set_value.call_args_list)
                assert len(list(returned_coins_message)) > 0
