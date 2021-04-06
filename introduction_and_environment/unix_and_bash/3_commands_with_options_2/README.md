# Command Basics 3

## Problem Description
The list below contains a number of variable names, as well as a text description of many different **bash** commands. Assign the name of the correct **bash** command, as a lowercase Python string, to each corresponding variable. These are harder than the first few, as they may contain additional arguments to be included with the command name.  

Unnecessary spaces will result in failed tests, make sure not to leave trailing spaces in the solutions!

For example:  
Variable: `ONE`  
Description: Command used when you remember the name of a **bash** command named "test", but forget what it does

In *solution.py* you would write:
```python
EXAMPLE = 'man test'
```

Variable: `ONE`  
Description: Search the contents of a file named "book.txt" for occurrences of the pattern "elephant"  

Variable: `TWO`  
Description: Move a file named "notes.txt" from the current directory to a directory named "newdir"   

Variable: `THREE`  
Description: Search all files in a directory named "testdir" for the pattern "string"  

Variable: `FOUR`  
Description: Delete an empty directory named "empty"  

Variable: `FIVE`  
Description: Navigate to our user's home directory (regardless of user's name)  

Variable: `SIX`  
Description: Delete a non-empty directory, named "Downloads", as well as all of its contents  

## Testing
* to test your solution, type 'pytest' within the **solutions** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory in this directory
