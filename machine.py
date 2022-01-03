from src.Machine import Machine

machine = Machine()
transaction = machine.start()


def get_machine():
    return machine


def get_transaction():
    return transaction
