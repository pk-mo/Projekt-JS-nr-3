class OnlyCalculatedAmountException(Exception):
    """Exception used to indicate only calculated amount of money can be inserted to machine."""

    def __init__(self):
        super().__init__("Only calculated amount of money")
