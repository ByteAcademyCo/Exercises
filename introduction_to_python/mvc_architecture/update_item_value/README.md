#  MVC Update Item Value 

## Motivation
Controller handles the user request. Typically, user interact with View, which in-turn raises appropriate URL request, this request will be handled by a controller. The controller renders the appropriate view with the model data as a response.

## Problem Description
Construct a MVC to update an existing key value from a dictionary object of different programming languagues while having below conditions:

'model' create a dict object `program_list` containing indexing of different programming languagues. Create 2 functions `get_list` to get the list object ,`update_list_key` to update the key value and return.

'app' containing logic related to the controller where objects `program_list` to capture list from model and show to user, `key` to capture key name from user for performing updation and `value` to capture new key value from user view. Create object `new_list` which peforms a function call to model to return the updated list. 

'view' containing functions `show_list`,`update_key`, `enter_value` and `display` to input/output values from/to the user interface. 


## Testing
* done

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory
