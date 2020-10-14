def make_change_helper(amount, denominations, num_coins):
    # if amount is 0 we made all the change and we return num_coins.
    if amount == 0:
        return num_coins
    # itterate through denominations from largest to smallest
    for i in range(len(denominations)):
        # if the amount is larger or equal to the current coin value
        # we recurse, decreasing the amount by that coin value, and 
        # increasing the number of coins by 1.
        if amount >= denominations[i]:
            return make_change_helper(amount-denominations[i], denominations, num_coins+1)
    # once we've itterated through all the coins we never hit amount == 0, so we
    # have a remainder we could not make change for and we return -1.
    return -1

def make_change(amount, denominations):
    # Sort denominations in decreasing order 
    denominations = sorted(denominations, reverse=True)
    return make_change_helper(amount, denominations, 0)
