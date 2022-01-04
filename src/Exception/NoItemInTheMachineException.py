class NoItemInTheMachineException(Exception):
    """Exception used to indicate no item in the machine."""

    def __init__(self):
        super().__init__("There is no item in the machine")
