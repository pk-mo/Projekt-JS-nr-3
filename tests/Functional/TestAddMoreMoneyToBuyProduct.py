from machine import get_machine
from tests.TestCase import TestCase
from tests.Utils import *


class TestAddMoreMoneyToBuyProduct(TestCase):
    def test(self):
        with gui_mock() as gui:
            machine = get_machine()
            item_id = 31
            price = machine.get_product_price(item_id)

            InsertCoins.input_callback(Coin.Coin(1))
            SelectProduct.input_callback(str(item_id))
            assert_gui_message_rendered('Too small money amount', gui)

            for _ in range(price - 1):
                InsertCoins.input_callback(Coin.Coin(1))

            assert_gui_message_rendered('Successful purchase of item with id ' + str(item_id), gui)
            assert_gui_message_pattern_not_rendered('^Returned change: .*$', gui)
