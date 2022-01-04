class InvalidItemIdException(Exception):
    """Exception used to indicate invalid item id."""

    def __init__(self):
        super().__init__("Invalid item id")
