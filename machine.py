from src.Machine import Machine

machine = Machine()
transaction = machine.start()


def get_machine():
    return machine


def get_transaction():
    return transaction


def reset_machine():
    global machine, transaction
    machine = Machine()
    transaction = machine.start()
