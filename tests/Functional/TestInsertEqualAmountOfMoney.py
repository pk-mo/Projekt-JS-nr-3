from machine import get_machine
from tests.TestCase import TestCase
from tests.Utils import *


class TestInsertEqualAmountOfMoney(TestCase):
    def test(self):
        with gui_mock() as gui:
            machine = get_machine()
            item_id = 38
            price = machine.get_product_price(item_id)

            buy_product(item_id, price)
            assert_gui_message_rendered('Successful purchase of item with id ' + str(item_id), gui)
            assert_gui_message_pattern_not_rendered('^Returned change: .*$', gui)
