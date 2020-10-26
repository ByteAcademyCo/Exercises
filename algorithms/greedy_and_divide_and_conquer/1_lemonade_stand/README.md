# Greedy Algorithm - Lemonade Stand

## Motivation
A greedy algorithm is a type of algorithm that builds up a solution piece by piece always choosing the piece that offers the most imediate benifit. We choose the locally optimal solution at each step to get a globally optimal solution to the problem.


## Problem Description
You have a lemonade stand and you are selling each glass of lemonade for 5$. You have a list of customers each wanting to buy one glass of lemonade, the customers in the list are in order of when they come to your stand. Customers can pay using either 5$, 10$, or 20$ bills. You start your day with no change or bills in your cash register. 
In the *solution.py* file, define a function `lemonade_change` that consumes a list of integers `customer_bills` representing the bill denomination each customer would like to pay with. Return `True` if you are able to make change for all the customers, and `False` otherwise.

## Example
```
customer_bills = [5, 10, 5, 20]
lemonade_change(customer_bills) == True

customer_bills = [5, 20, 10]
lemonade_change(customer_bills) == False
```
In the first example, the first customer buys one glass for 5$, so we now have 5$ in our register. The next customer buys one glass and gives us a 10$ bill, so we give him our 5$ bill and we now have one 10$ bill in our register. The third customer buys one glass for 5$, so we now have one 10$ bill and one 5$ bill in our register. The last customer comes and buys one glass and gives us a 20$ bill and we can give him our 10$ bill and our 5$ bill as change in return.

In the second example, when the second customer comes to our stand they want to pay with a 20$ bill, but we only have one 5$ bill in our register so we cannot make change for him.




## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory within this directory
