from ..Exception import *


class Item:
    """Represents any item, that can be contained in machine."""

    def __init__(self, item_id: int, price: int):
        """Item constructor. Requires item id and price in gr."""
        self.id = item_id
        self.price = price
        self.__validate()

    def __validate(self) -> None:
        """Validates Item entity."""
        self.__validate_id()
        self.__validate_price()

    def __validate_id(self) -> None:
        """Validates Item id."""
        if self.id < 30 or self.id > 50:
            raise InvalidItemIdException()

    def __validate_price(self) -> None:
        """Validates Item price."""
        if self.price == 0:
            raise InvalidItemPriceException()
