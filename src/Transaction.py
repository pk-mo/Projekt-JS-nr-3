from Entity import *


class Transaction:
    """Represents transaction, that can occur in the machine."""

    def insert_coin(self, coin: Coin) -> None:
        """Inserts one coin to machine and current transaction."""
        pass

    def get_inserted_money_amount(self) -> int:
        """Returns amount of inserted money."""
        pass

    def interrupt(self) -> None:
        """Interrupts transaction and returns all coins."""
        pass

    def select_item(self, item_id: int) -> None:
        """Selects the item with specified id for purchase."""
        pass

    def get_selected_item_id(self) -> int:
        """Returns id of selected item."""
        pass
