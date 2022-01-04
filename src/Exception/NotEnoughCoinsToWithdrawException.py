class NotEnoughCoinsToWithdrawException(Exception):
    def __init__(self):
        super().__init__("There is not enough coins in the machine to withdraw")
