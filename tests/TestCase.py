import unittest
from unittest import mock

from machine import reset_machine
from src.Presentation import SelectProduct


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        reset_machine()

    def tearDown(self) -> None:
        with mock.patch('src.Presentation.SelectProduct.dpg'):
            with mock.patch('src.Presentation.InsertCoins.dpg'):
                SelectProduct.abort()
                SelectProduct.clear()
