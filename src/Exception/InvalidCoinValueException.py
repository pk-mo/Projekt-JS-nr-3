class InvalidCoinValueException(Exception):
    """Exception used to indicate invalid coin value."""

    def __init__(self):
        super().__init__("Invalid coin value")
