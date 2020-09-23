def make_change_helper(amount, denominations, denomination_keys, num_coins):
    # if we have ammount 0, we made all the change and we return num_coins.
    if amount == 0:
        return num_coins
    # we itterate through the denomination_keys list by index and the denomination key
    for idx, k in enumerate(denomination_keys):
        # if amount is greater than the denomination key
        if amount >= k:
            # we update the denomination dict taking one away
            denominations[k] -= 1
            # if we now have none of that coin left in our denominations dict
            # we update the list by removing that element and only looking at the 
            # denominations in the rest of the list.
            if denominations[k] == 0:
                denomination_keys = denomination_keys[idx+1:]
            # we recurse, updating the amount by subtracting the coin we saw, and
            # adding one to num_coins
            return make_change_helper(amount-k, denominations, denomination_keys, num_coins+1)
    # if we itterated through all the coins and still have a remainder, we could not
    # make all the change, so we return -1.
    return -1

def make_change(amount, denominations):
    # create a list of denomination values sorted in decreasing order.
    denomination_keys = sorted(denominations.keys(), reverse=True)
    return make_change_helper(amount, denominations, denomination_keys, 0)
