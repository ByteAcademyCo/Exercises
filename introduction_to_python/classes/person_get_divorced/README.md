# Person Class Method - Get Divorced

# Problem Description
Using your `Person` class and `Child` class you defined in a previous question, define a method, `get_divorced`, and if the person is married,sets the spouse of the person and their spouse to be `None`.

 ## Example
 ```
 John = Person("John", 31, Kathy, [])
 Kathy = Person("Kathy", 29, John, [])
 John.get_divorced() == None
 John.spouse == None
 Kathy.spouse == None
 ```

## Testing
* To test your solution, type 'pytest' within the solution subdirectory


## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory