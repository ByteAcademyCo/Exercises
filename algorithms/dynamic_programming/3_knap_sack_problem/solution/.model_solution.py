def knap_sack(x, items):
    num_items = len(items)
    wt_lst = []
    val_lst = []
    for v,w in items.values():
        val_lst.append(v)
        wt_lst.append(w)
    
    # Create an x by len(items) array to keep track of max_value if you keep 
    # items[i] if you have a weight of i. 
    K = [[0 for i in range(x + 1)] for i in range(num_items + 1)]

    for i in range(num_items + 1): 
        for w in range(x + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt_lst[i-1] <= w: 
                K[i][w] = max(val_lst[i-1] + K[i-1][w-wt_lst[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
    for k in K:
        print(k)
    print(x)
    print(num_items)
    return K[num_items][x]

print(knap_sack(5, {"hat": (1,2), "sunscreen": (3,2), "food": (6,4), "water": (5,3)}))