class TooSmallMoneyAmountException(Exception):
    def __init__(self, is_item_in_machine=True):
        if is_item_in_machine:
            super().__init__("Too small money amount")
        else:
            super().__init__("Too small money amount, product has ended in the machine")

