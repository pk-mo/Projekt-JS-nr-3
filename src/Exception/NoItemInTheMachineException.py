class NoItemInTheMachineException(Exception):
    def __init__(self):
        super().__init__("There is no item in the machine")
