from machine import get_machine
from tests.TestCase import TestCase
from tests.Utils import *


class TestBuyAllProductsOfOneType(TestCase):
    def test(self):
        with gui_mock() as gui:
            machine = get_machine()
            item_id = 36
            price = machine.get_product_price(item_id)

            for _ in range(5):
                buy_product(item_id, price)

            no_item_in_machine_message = 'There is no item in the machine'
            assert_gui_message_not_rendered(no_item_in_machine_message, gui)

            buy_product(item_id, price)
            assert_gui_message_rendered(no_item_in_machine_message, gui)
