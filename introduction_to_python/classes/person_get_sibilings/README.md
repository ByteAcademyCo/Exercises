# Person Class Method - Give Birth

# Problem Description
Using your `Person` class and `Child` class you defined in a previous question, define a method inside the child class, `get_siblings`, that returns a list of names of all the siblings of the child object sorted in increasing order by age.
Hint: Note that a child can have a half sibling which is a child of one parent but not the other.

 ## Example
 ```
 Jonny = Person("Jonny", 32, Beth, [Max, Annie, Ron])
 Beth = Person("Beth", 28, Jonny, [Max, Annie, Ron])
 Max = Child("Max", 5, None, [], [Beth, Jonny])
 Annie = Child("Annie", 10, None, [], [Beth, Jonny])
 Ron = Child("Ron", 7, None, [], [Beth, Jonny])
 Max.get_siblings() == ["Ron", "Annie"]
 ```

## Testing
* To test your solution, type 'pytest' within the solution subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory