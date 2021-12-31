class InvalidCoinValueException(Exception):
    def __init__(self):
        super().__init__("Invalid coin value")
