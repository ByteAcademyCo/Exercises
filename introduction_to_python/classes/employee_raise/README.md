# Employee Class - Give Raises

# Problem Description
Define a function `give_raises` that consumes `employee_lst`, a list of employee objects as defined in the previous question, and mutates each employee object in the list such that each employee is given a raise to their salary according to the following criteria:
* An employee gets a raise of $5,000 if they have been at the company for <= 5 years.
* An employee gets a raise of $8,000 if they have been at the company for > 5 and < 10 years.
* An employee gets a raise of $10,000 if they have been at the company for >= 10 years.

## Example
```
emp1 = Employee("John", 1, 45000, 8)
emp2 = Employee("Jane", 2, 22000, 1)
emp3 = Employee("Marie", 3, 90000, 10)

give_raises([emp1, emp2, emp3]) == None
emp1.salary == 53000
emp2.salary == 27000
emp3.salary == 100000

```


## Testing
* To test your solution, type 'pytest' within the solution subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory