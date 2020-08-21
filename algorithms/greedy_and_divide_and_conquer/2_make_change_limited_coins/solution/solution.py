def help_make_change(amount, denominations, denomination_keys, number_of_coins):
    # if we have ammount 0, we made all the change and we return num_coins.
    if amount == 0:
        return number_of_coins
    # we itterate through the denomination_keys list by index and the denomination key
    for index, keys in enumerate(denomination_keys):
        # if amount is greater than the denomination key
        if amount >= keys:
            # we update the denomination dict taking one away
            denominations[keys] -= 1
            # if we now have none of that coin left in our denominations dict
            # we update the list by removing that element and only looking at the 
            # denominations in the rest of the list.
            if denominations[keys] == 0:
                denomination_keys = denomination_keys[index + 1:]
            # we recurse, updating the amount by subtracting the coin we saw, and
            # adding one to num_coins
            return help_make_change(amount - keys, denominations, denomination_keys, number_of_coins + 1)
    # if we itterated through all the coins and still have a remainder, we could not
    # make all the change, so we return -1.
    return -1
def make_change(amount, denominations):
    # create a list of denomination values sorted in decreasing order.
    denomination_keys = sorted(denominations.keys(), reverse=True)
    return help_make_change(amount, denominations, denomination_keys, 0)