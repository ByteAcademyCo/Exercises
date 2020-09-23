def knap_sack(x, items):
    num_items = len(items)
    wt_lst = []
    val_lst = []
    # get the weight and values of each item in val_lst and wt_lst.
    for v,w in items.values():
        val_lst.append(v)
        wt_lst.append(w)
    
    # Create a len(items) by x array to keep track of the max_val once 
    # you've looked at all items up to the ith item if you have a weight of w. 
    K = [[0 for i in range(x + 1)] for i in range(num_items + 1)]

    # for i from 0 to num_items
    for i in range(num_items + 1):
        # for weight from 0 to x 
        for w in range(x + 1): 
            # when we hae no items and weight 0, we have 0 value in our bag
            if i == 0 or w == 0: 
                K[i][w] = 0
            # if the weight of the ith item is less than or equal to current
            # weight w, the max value we can add is either the val of the ith
            # item + the max-val of all the i-1 elements and weight - weight of ith 
            # element or the value of all the i-1 elements with current weight.
            elif wt_lst[i-1] <= w:
                # note that the val and weight of the ith element is at position i-1
                # in val_lst and wt_lst.
                K[i][w] = max(val_lst[i-1] + K[i-1][w-wt_lst[i-1]],  K[i-1][w]) 
            else:
                # if the weight of the ith element is greater than w, we cannot use it
                # so the max value we can have is just the maximum value we found for
                # all the i-1 elements with current weight w.
                K[i][w] = K[i-1][w] 
    return K[num_items][x]