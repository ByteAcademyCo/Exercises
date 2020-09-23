# Inventory Dictionary - Stock Price

## Problem Description 
You own a store with a variety of products on stock in diffrent quantities. Define a Python function `inventory_price`, which consumes a dictionary `idict`, where the keys are strings representing the names of your products, and the values are tuples `(quantity, price)`, where `quantity` is an integer and `price` is a float. Output the total price of the inventory in your store.

## Example
```
idict = {"hat": (20, 15.50), "tshirt": (50, 19.99), "jeans": (10, 69.55)}
inventory_price(idict) == 2005.0
```

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory