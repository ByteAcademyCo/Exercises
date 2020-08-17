def make_change_helper(amount, denominations, denomination_keys, num_coins):
    if amount == 0:
        return num_coins
    for idx, k in enumerate(denomination_keys):
        if amount >= k:
            denominations[k] -= 1
            if denominations[k] == 0:
                denomination_keys = denomination_keys[idx+1:]
            return make_change_helper(amount-k, denominations, denomination_keys, num_coins+1)
    return -1

def make_change(amount, denominations):
    denomination_keys = sorted(denominations.keys(), reverse=True)
    return make_change_helper(amount, denominations, denomination_keys, 0)

denominations = {1: 5, 2: 1, 10: 5, 50: 3, 100: 1, 200: 1}
print(make_change(450, denominations))

denominations3 = {1: 5, 2: 1, 5: 1, 10: 1, 20: 1, 50: 3}
print(make_change(43, denominations3))

denominations2 = {1: 5, 2: 1, 50: 3, 100: 1, 200: 1}
print(make_change(305, denominations2))