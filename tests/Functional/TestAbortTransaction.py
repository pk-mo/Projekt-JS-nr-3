from tests.TestCase import TestCase
from tests.Utils import *


class TestAbortTransaction(TestCase):
    def test(self):
        with gui_mock() as gui:
            self.__insert_coins()
            SelectProduct.abort()
            assert_gui_message_rendered('Returned coins: 1.0zl, 2.0zl, 5.0zl', gui)

    def __insert_coins(self):
        InsertCoins.input_callback(Coin.Coin(100))
        InsertCoins.input_callback(Coin.Coin(200))
        InsertCoins.input_callback(Coin.Coin(500))
