# Age Range Dictionary  

## Problem Description 
Define a Python function `remove_ages` which consumes a dictionary `pdict`, and two non-negative integers `x` and `y` where `x <= y`. The keys in `pdict` are strings representing names of people, and the values are non-negative integers representing the age of the person. Return a dictionary with all the key-value pairs in `pdict` where the age falls inside of the range `[x,y]`.

## Examples
```
pdict = {"Nell": 26, "Sue": 30, "Billy": 4}
remove_ages(pdict, 10, 30) == {"Nell": 26, "Sue": 30}
```


## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory