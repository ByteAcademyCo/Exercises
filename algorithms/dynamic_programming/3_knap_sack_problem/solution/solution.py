def knap_sack(x, items):
    num_items = len(items)
    wt_lst = []
    val_lst = []
    for v,w in items.values():
        val_lst.append(v)
        wt_lst.append(w)
    
    # Create a len(items) by x array to keep track of the max_val once 
    # you've looked at all items up to the ith item if you have a weight of w. 
    K = [[0 for i in range(x + 1)] for i in range(num_items + 1)]

    for i in range(num_items + 1): 
        for w in range(x + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt_lst[i-1] <= w: 
                K[i][w] = max(val_lst[i-1] + K[i-1][w-wt_lst[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
    return K[num_items][x]

print(knap_sack(5, {"hat": (1,2), "sunscreen": (3,2), "food": (6,4), "water": (5,3)}))