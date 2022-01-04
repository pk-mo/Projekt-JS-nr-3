from src.Machine import Machine

machine = Machine()
transaction = machine.start()


def get_machine():
    """Gets the machine object."""
    return machine


def get_transaction():
    """Gets the transaction object."""
    return transaction


def reset_machine():
    """Resets the machine and starts a new transaction."""
    global machine, transaction
    machine = Machine()
    transaction = machine.start()
