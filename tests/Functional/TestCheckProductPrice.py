from tests.TestCase import TestCase
from tests.Utils import *


class TestCheckProductPrice(TestCase):
    def test(self):
        with gui_mock() as gui:
            SelectProduct.input_callback("3")
            SelectProduct.input_callback("5")
            assert_gui_message_pattern_rendered('^Price: \d+\.\d*zl$', gui)
