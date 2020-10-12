#  MVC Update List 

## Motivation
Model represents shape of the data and business logic. It maintains the data of the application. Model objects retrieve and store model state in a database.

The model is responsible for managing the data of the application. It responds to the request from the view and it also responds to instructions from the controller to update itself.


## Problem Description
Construct a MVC to update a fruit item from a list  of user_defined fruits while having below conditions:

'model' create a list object `fruits` containing different fruit items  and functions `get_store` to return list of fruits ,`update_fruit` to delete a specific item. 

'app' containing logic related to the controller where objects `fruits` , `fruit` are used to capture fruit list from model and ask user input to add a particular fruit to the list after viewing list from object `show` which outputs the list of fruits to view. Peform a function call to model to add the data item to original list and create object `data` to contain the new list of fruits to the view. 

'view' containing functions `show_fruits`and`ask_fruit`  to input/output values from/to the user interface. 


## Testing
* done

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory
