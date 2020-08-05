# Basic Inheritance Implementation

# Problem Description
 Write a simple program to implement inheritance. Write two classes `Person` and `Employee`. `Person` is the parent class and `Employee` should inherit from `Person`. 
 In the `Person` class:
 * Set the `name` (a string) in the constructor function.
 * Define a method `getName` that returns the name of the `Person`.
 * Define a method `isEmployee()` that returns `False` for a person that is not an employee.
 * Use the magic method `__str__()` to create a nice string representation of our `Person` objects, so that when we print a `Person` object, we print `Person(name=NAME)`, where `NAME` is the name of the given person. 

  In the `Employee` class:
 * Employee should inherit from the `Person` class.
 * Define a method `isEmployee()` that returns `True` for a person that is an employee.
 * Use the magic method `__str__()` to create a nice string representation of our `Employee` objects, so that when we print an `Employee` object, we print `Employee(name=NAME)`, where `NAME` is the name of the given employee. 


For Example:
```
Person("Jane Doe").getName() => "Jane Doe"
Person("Jane Doe").isEmployee() => False
print(Person("Jane Doe")) prints out "Person(name=Jane Doe)"

Employee("John Doe").getName() => "John Doe"
Employee("John Doe").isEmployee() => True
print(Employee("John Doe")) prints out "Employee(name=John Doe)
```

## Testing
* To test your solution, type 'pytest' within the solution subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory