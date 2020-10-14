def inventory_price(idict):
    # varible to store the price
    price = 0
    for product in idict.values():
        price += product[0]*product[1]
    return price