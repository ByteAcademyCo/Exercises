
def make_change_helper(amount, denominations, num_coins):
    for i in range(len(denominations)-1, -1, -1):
        if amount >= denominations[i]:
            if num_coins == -1:
                num_coins += 1
            return make_change_helper(amount-denominations[i], denominations, num_coins+1)
    return num_coins

def make_change(amount, denominations):
    return make_change_helper(amount, denominations, -1)




denominations = [1, 2, 5, 10, 20, 50, 100, 200]
print(make_change(450, denominations))