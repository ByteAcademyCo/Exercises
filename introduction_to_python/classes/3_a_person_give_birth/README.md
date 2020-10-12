# Person Class Method - Give Birth

# Problem Description
Using your `Person` class and `Child` class you defined in a previous question, define a method, `give_birth`, that consumes `self` and a string `name` and updates the child lists of self and their spouse, if they have a spouse, to contain a new child object with name `name`, age `0`, having no spouse and no children, with parents `self` and the spouse of self, if they have a spouse or None as the second parent.

 ## Example
 ```
 Jonny = Person("Jonny", 32, None, [])
 Beth = Person("Beth", 28, Jonny, [])
 Jonny.spouse = Beth
 Beth.give_birth("Sam") == None
 Beth.children = [Child("Sam", 0, None, [], (Beth, Jonny))]
 ```

## Testing
* To test your solution, type 'pytest' within the solution subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory