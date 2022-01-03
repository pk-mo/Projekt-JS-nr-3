from unittest import mock

from tests.TestCase import TestCase
from src.Entity import Coin
from src.Presentation import SelectProduct, InsertCoins
from machine import get_machine


class TestInsertBiggerAmountOfMoney(TestCase):
    def test(self):
        with mock.patch('src.Presentation.SelectProduct.dpg') as dpg:
            with mock.patch('src.Presentation.InsertCoins.dpg') as coins_dpg:
                machine = get_machine()
                item_id = 37
                price = machine.get_product_price(item_id)

                for _ in range(price):
                    InsertCoins.input_callback(Coin.Coin(1))
                SelectProduct.input_callback(str(item_id))

                for _ in range(price - 1):
                    InsertCoins.input_callback(Coin.Coin(1))
                InsertCoins.input_callback(Coin.Coin(5))
                SelectProduct.input_callback(str(item_id))
                assert dpg.set_value.called is True

                successful_purchase_message = 'Successful purchase of item with id ' + str(item_id)
                successful_purchase_call = filter(
                    lambda call_args: call_args.args[1] == successful_purchase_message,
                    dpg.set_value.call_args_list)
                assert len(list(successful_purchase_call)) > 0

                returned_change_message = filter(
                    lambda call_args: call_args.args[1] == "Returned change: 0.01zl, 0.01zl, 0.01zl, 0.01zl",
                    coins_dpg.set_value.call_args_list)
                assert len(list(returned_change_message)) > 0

