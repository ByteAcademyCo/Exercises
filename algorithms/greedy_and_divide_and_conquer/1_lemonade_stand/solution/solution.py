def lemonade_change(customer_bills):
    register = {5: 0, 10: 0, 20: 0}
    for bill in customer_bills:
        if bill == 5:
            register[5] +=1
        elif bill == 10:
            if not register[5] == 0:
                register[5] -= 1
                register[10] += 1
            else:
                return False
        elif bill == 20:
            if register[10] == 0:
                if register[5] >= 3:
                    register[5] -= 3
                    register[20] +=1
                else:
                    return False
            elif register[10] >= 1 and register[5] >= 1:
                register[10] -= 1
                register[5] -= 1
                register[20] += 1
            else:
                return False
    return True

print(lemonade_change([5, 20, 5, 20]))
