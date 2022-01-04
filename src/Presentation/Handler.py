from . import SelectProduct, InsertCoins


def handle():
    """Handles whole presentation layer."""
    SelectProduct.render()
    InsertCoins.render()
