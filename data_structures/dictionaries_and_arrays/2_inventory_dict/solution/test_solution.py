def test_solution():
    from solution import inventory_price

    idict = {"hat": (20, 15.50), "tshirt": (50, 19.99), "jeans": (10, 69.55)}
    assert inventory_price(idict) == 2005
    assert inventory_price({"hat": (20, 15.50)}) == 310
    assert inventory_price({}) == 0
