import re
from unittest import mock

from machine import get_machine
from src.Entity import Coin
from src.Presentation import SelectProduct, InsertCoins
from tests.TestCase import TestCase


class TestAddMoreMoneyToBuyProduct(TestCase):
    def test(self):
        with mock.patch('src.Presentation.SelectProduct.dpg') as dpg:
            with mock.patch('src.Presentation.InsertCoins.dpg') as coins_dpg:
                machine = get_machine()
                item_id = 31
                price = machine.get_product_price(item_id)

                InsertCoins.input_callback(Coin.Coin(1))
                SelectProduct.input_callback(str(item_id))
                assert dpg.set_value.called is True

                too_small_money_amount_message = 'Too small money amount'
                too_small_money_amount_call = filter(
                    lambda call_args: call_args.args[1] == too_small_money_amount_message,
                    dpg.set_value.call_args_list)
                assert len(list(too_small_money_amount_call)) > 0

                for _ in range(price - 1):
                    InsertCoins.input_callback(Coin.Coin(1))

                successful_purchase_message = 'Successful purchase of item with id ' + str(item_id)
                successful_purchase_call = filter(
                    lambda call_args: call_args.args[1] == successful_purchase_message,
                    dpg.set_value.call_args_list)
                assert len(list(successful_purchase_call)) > 0
                
                returned_change_message = filter(
                    lambda call_args: re.search('^Returned change: .*$', call_args.args[1]),
                    coins_dpg.set_value.call_args_list)
                assert len(list(returned_change_message)) == 0
