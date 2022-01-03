import re
from unittest import mock

from src.Presentation import SelectProduct
from tests.TestCase import TestCase


class TestCheckProductPrice(TestCase):
    def test_too_high_id(self):
        with mock.patch('src.Presentation.SelectProduct.dpg') as dpg:
            SelectProduct.input_callback("29")
            assert dpg.set_value.called is True
            price_message_call = filter(lambda call_args: call_args.args[1] == 'Invalid item id',
                                        dpg.set_value.call_args_list)
            assert len(list(price_message_call)) > 0

    def test_too_low_id(self):
        with mock.patch('src.Presentation.SelectProduct.dpg') as dpg:
            SelectProduct.input_callback("51")
            assert dpg.set_value.called is True
            price_message_call = filter(lambda call_args: call_args.args[1] == 'Invalid item id',
                                        dpg.set_value.call_args_list)
            assert len(list(price_message_call)) > 0
