class NotEnoughCoinsToWithdrawException(Exception):
    """Exception used to indicate not enough coins to withdraw."""

    def __init__(self):
        super().__init__("There is not enough coins in the machine to withdraw")
