from machine import get_machine
from tests.TestCase import TestCase
from tests.Utils import *


class TestInsertBiggerAmountOfMoney(TestCase):
    def test(self):
        with gui_mock() as gui:
            machine = get_machine()
            item_id = 37
            price = machine.get_product_price(item_id)

            # Buy product before to be sure, that there will be enough coins for change in the machine
            buy_product(item_id, price)
            self.__buy_product_with_returned_change(item_id, price)

            assert_gui_message_rendered('Successful purchase of item with id ' + str(item_id), gui)
            assert_gui_message_rendered("Returned change: 0.01zl, 0.01zl, 0.01zl, 0.01zl", gui)

    def __buy_product_with_returned_change(self, item_id: int, price: int):
        for _ in range(price - 1):
            InsertCoins.input_callback(Coin.Coin(1))
        InsertCoins.input_callback(Coin.Coin(5))
        SelectProduct.input_callback(str(item_id))
