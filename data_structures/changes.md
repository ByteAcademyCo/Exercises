# Second Iteration Changes

**Main things to look for**

1) Differentiate public/private tests
In the second iteration, we want more comprehensive tests that can test a) edge cases b) invalid inputs c) runtime constraints. The directory structure should also reflect this change and be structured in a specific format. Please reference [this](https://github.com/ByteAcademyCo/Introduction-To-Python/tree/master/exercises/recursive_functions/2_fibonacci/solution) section for a template on directory structure and comprenhensive tests.

2) Templated problem description. 
Each section should have a standardized problem description. It is almost ALWAYS asking them to define a function, the only exceptions being the modules before they learn what a function is. Here is the problem description template:
```
Define a Python function named A that consumes a B C and returns D.
```
where `A` is the name of the function. `B` is the type of `C`. `C` is the name of the argument. There can be many `B`-`C` pairs, one for each argument. `D` is a sentence that references `C`.
Please look in the recursie functions section to see a completed section following [this](https://github.com/ByteAcademyCo/Introduction-To-Python/tree/master/exercises/recursive_functions) template if you would like a reference.

3) Include examples in the READMEs. Just a basic snippet like. These should also be the public tests.
```
assert factorial(3) == 6
```

4) Omit the testing portion of the `README.md` file. Pretty self explanatory - this is the file the student views, this testing portion holds no value.

5) Naming conventions for files/directories. All `README.md` files should be capitalized as shown. All `.py` files should be in `lowercase_snakecase.py` format, all directories should be the same (currently a lot of solutions directories start with capital S)

6) The main `README.md` file for the section that contains all the exercises should have a valid id-exercise mapping with appropriate links. The links in the table simply point to the folder containing the exercise, see https://github.com/ByteAcademyCo/Introduction-To-Python/tree/master/exercises/recursive_functions as a template.
