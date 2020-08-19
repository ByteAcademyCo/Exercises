def help_make_change(amount, denominations, denomination_keys, number_of_coins):
    if amount == 0:
        return number_of_coins
    for index, keys in enumerate(denomination_keys):
        if amount >= keys:
            denominations[keys] -= 1
            if denominations[keys] == 0:
                denomination_keys = denomination_keys[index + 1:]
            return help_make_change(amount - keys, denominations, denomination_keys, number_of_coins + 1)
    return -1
def make_change(amount, denominations):
    denomination_keys = sorted(denominations.keys(), reverse=True)
    return help_make_change(amount, denominations, denomination_keys, 0)