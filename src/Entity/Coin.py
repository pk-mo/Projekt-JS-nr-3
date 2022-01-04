from ..Exception import *


def get_valid_coin_values() -> [int]:
    """Returns list of valid coin values."""
    return [1, 2, 5, 10, 20, 50, 100, 200, 500]


class Coin:
    """Represents any coin, that can be inserted into machine."""

    def __init__(self, value: int):
        """Coin constructor. Coin value must be in gr."""
        self.value = value
        self.__validate()

    def __validate(self) -> None:
        """Validates Coin value."""
        if self.value not in get_valid_coin_values():
            raise InvalidCoinValueException()

    def get_value(self):
        """Gets the coin value."""
        return self.value
