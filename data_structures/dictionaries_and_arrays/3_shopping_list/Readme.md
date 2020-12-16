# Shopping List - Cheapest Store 

## Problem Description 
You are going grocery shopping and want to find the cheapest grocery store to shop at. Define a python function `cheapest_store`, that consumes a non-empty dictionary, `grocery_dict` and a list, `shopping_list`. `grocery_dict` will have strings as keys which are the names of grocery stores, and that values for each key are also a dictionary, where the keys are names of products as strings and the values are the price of each product as a float. `shopping_list` will be a list of string names of all the products you want to buy. Output the name of the store where you can buy your groceries for the cheapest amount of money. If a store doesn't carry a product on your grocery list, add a penalty of `$5` to your total spenditure at that store. If two stores are tied, return the store with the name that comes first lexicographically.

## Examples
```
grocery_dict = {"Walmart": {"pasta": 2.0,
                            "bread": 1.5,
                            "cheese": 6.0,
                            "ketchup": 3.0,
                            "salami": 9.0,
                            "onions": 1.0},
                "Thriftys": {"bread": 4.0,
                             "ham": 6.0,
                             "salami": 12.0,
                             "pasta": 1.75,
                             "mayo": 4.0,
                             "onions": 2.0,
                             "ketchup": 3.5}
                }
shopping_list = ["ham", "salami", "ketchup", "mayo", "pasta", "cheese", "tuna"]
cheapest_store(grocery_store, shopping_list) == "Walmart"
```

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory