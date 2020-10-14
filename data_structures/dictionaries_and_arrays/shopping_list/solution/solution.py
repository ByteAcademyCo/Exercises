from math import inf

def grocery_cost(store_items, shopping_list):
    total_cost = 0
    for item in shopping_list:
        if item in store_items:
            total_cost += store_items[item]
        else:
            total_cost += 5
    return total_cost

def cheapest_store(grocery_store, shopping_list):
    min_cost = inf
    min_store = ""
    for store, store_items in grocery_store.items():
        store_cost = grocery_cost(store_items, shopping_list)
        if store_cost < min_cost:
            min_cost = store_cost
            min_store = store
        elif store_cost == min_cost and store < min_store:
            min_store = store
    return min_store
