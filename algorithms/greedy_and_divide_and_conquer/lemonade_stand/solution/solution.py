def lemonade_change(customer_bills):
    # we create a dictionary to keep track of all the bills 
    # of each denomination in our register.
    # we start with 0 of each bill.
    register = {5: 0, 10: 0, 20: 0}
    # we itterate through the list of customer_bills
    for bill in customer_bills:
        # if the bill is 5, we don't need any change
        # so we serve them lemodane and add the 5$ bill
        # to our register updating the dictionary at 5 by 1.
        if bill == 5:
            register[5] +=1
        # if the bill is 10, we need to check if we have any 
        # 5$ bills to make change for the customer.
        elif bill == 10:
            # If we have a 5,
            # we update the register removing a 5 an adding a 10$ bill.
            if not register[5] == 0:
                register[5] -= 1
                register[10] += 1
            else:
            # if we have no 5 bills we cannot make change and return false.
                return False
        # if the customer has a 20$ bill we need to try and make change with 10s or 5s.
        elif bill == 20:
            # if we have no 10s we need 3 5$ bills
            if register[10] == 0:
                if register[5] >= 3:
                    register[5] -= 3
                    register[20] +=1
                else:
                    return False
            # if we have a 10, we also need one 5$ bill.
            elif register[10] >= 1 and register[5] >= 1:
                register[10] -= 1
                register[5] -= 1
                register[20] += 1
            else:
                return False
    # once we've itterated through all customers, we were able to make all
    # the change so we return True.
    return True

print(lemonade_change([5, 20, 5, 20]))
