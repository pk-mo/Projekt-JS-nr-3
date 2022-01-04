from src.Presentation import SelectProduct
from tests.TestCase import TestCase
from tests.Utils import *


class TestCheckProductPrice(TestCase):
    def test_too_high_id(self):
        with gui_mock() as gui:
            SelectProduct.input_callback("29")
            assert_gui_message_rendered('Invalid item id', gui)

    def test_too_low_id(self):
        with gui_mock() as gui:
            SelectProduct.input_callback("51")
            assert_gui_message_rendered('Invalid item id', gui)
