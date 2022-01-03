from unittest import mock

from tests.TestCase import TestCase
from src.Entity import Coin
from src.Presentation import SelectProduct, InsertCoins
from machine import get_machine


class TestBuyAllProductsOfOneType(TestCase):
    def test(self):
        with mock.patch('src.Presentation.SelectProduct.dpg') as dpg:
            with mock.patch('src.Presentation.InsertCoins.dpg'):
                machine = get_machine()
                item_id = 36
                price = machine.get_product_price(item_id)

                for _ in range(6):
                    for _ in range(price):
                        InsertCoins.input_callback(Coin.Coin(1))
                    SelectProduct.input_callback(str(item_id))
                assert dpg.set_value.called is True

                no_item_in_machine_message = 'There is no item in the machine'
                no_item_in_machine_message_call = filter(
                    lambda call_args: call_args.args[1] == no_item_in_machine_message,
                    dpg.set_value.call_args_list)
                assert len(list(no_item_in_machine_message_call)) > 0
