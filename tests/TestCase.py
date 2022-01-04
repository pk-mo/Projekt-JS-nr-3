import unittest

from machine import reset_machine
from src.Presentation import SelectProduct
from tests.Utils import gui_mock


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        reset_machine()

    def tearDown(self) -> None:
        with gui_mock():
            SelectProduct.abort()
            SelectProduct.clear_selected_product()
