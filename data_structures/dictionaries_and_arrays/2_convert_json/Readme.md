# Convert JSON 

# Motivation 
`JavaScript Object Notation` (JSON) is a standardized format commonly used to transfer data as text that can be sent over a network. It's used by lots of APIs and Databases.

`json.dumps()` : The function is responsible for converting a python string into a json object

`json.loads()` : The function is responsible for converting a json object into a python string


## Problem Description 
Define a Python function named `convert` that consumes one parameter `dict`. The function returns the json format of the passed `dictionary`.

## Examples
```
dict = {"students": [{"firstName": "Nikki", "lastName": "Roysden"}]}
convert(dict)
dict = '{"students": [{"firstName": "Nikki", "lastName": "Roysden"}]}'
```

## Testing
* To test your solution, type 'pytest' within the **solution** subdirectory

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory