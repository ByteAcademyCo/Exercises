# Bash Operators

## Problem Description
The list below contains a number of variable names, as well as a text description of many different **bash** commands and operators that must be used. Assign the name of the correct **bash** command, as a lowercase Python string, to each corresponding variable. These are harder than the first few, and may need bash operators to pass data between commands or alter execution.  

Unnecessary spaces will result in failed tests, make sure not to leave trailing spaces in the solutions!

For example:  
Variable: `EXAMPLE`  
Description: Commands to list the contents of a directory, and then search that output for any files ending in ".py"  

In *solution.py* you would write:
```python
EXAMPLE = 'ls | grep .py'
```

Variable: `ONE`  
Description: Commands to create a directory named "testdir" and then navigate into that directory, if creation was successful  

Variable: `TWO`  
Description: Commands to view the entire contents of a file named "textfile.txt" and search that output for occurrences of the word "and"  

Variable: `THREE`  
Description: Commands to view the contents of the current directory, and then *append* that output to an existing text file named "contents.txt"  

Variable: `FOUR`  
Description: Commands to *either* navigate into a directory named "current", or, if that command failed, create the directory (but not bother with navigation afterwards)  

Variable: `FIVE`  
Description: Commands to view our command line's current directory path, and then write that output to a *new* file called "current_path.txt"  

## Testing
* to test your solution, type 'pytest' within the **solutions** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *solution* subdirectory in this directory
