class InvalidItemIdException(Exception):
    def __init__(self):
        super().__init__("Invalid item id")
