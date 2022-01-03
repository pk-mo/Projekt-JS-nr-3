class OnlyCalculatedAmountException(Exception):
    def __init__(self):
        super().__init__("Only calculated amount of money")

