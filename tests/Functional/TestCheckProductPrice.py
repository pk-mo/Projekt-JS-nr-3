import re
from unittest import mock

from src.Presentation import SelectProduct
from tests.TestCase import TestCase


class TestCheckItemPrice(TestCase):
    def test(self):
        with mock.patch('src.Presentation.SelectProduct.dpg') as dpg:
            SelectProduct.input_callback("3")
            SelectProduct.input_callback("5")
            assert dpg.set_value.called is True
            price_message_call = filter(lambda call_args: re.search('^Price: \d+\.\d*zl$', call_args.args[1]),
                                        dpg.set_value.call_args_list)
            assert len(list(price_message_call)) > 0
