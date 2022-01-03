from . import SelectProduct, InsertCoins, Buy, Products


def handle():
    SelectProduct.render()
    InsertCoins.render()
    Buy.render()
    Products.render()
