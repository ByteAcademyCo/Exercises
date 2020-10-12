#  MVC Delete Key

## Motivation
It has three components, namely 
a model that deals with the business logic,
a view for the user interface, and
a controller to handle the user input, manipulate data, and update the view.

## Problem Description
Construct a MVC to delete an item from a dictionary of user_defined movies while having below conditions:

'model' create a dict object `movie_list` containing key value pair of index followed by movie title and functions `get_list` to return list of movies ,`del_list_key` to delete a specific item. 

'app' containing logic related to the controller where objects `movie_list` , `del_key` are used to capture list from model and ask user choice to delete a particular item from view. Peform a function call to model to delete the data item from original list and return the new list of movies to the view. 

'view' containing functions `delete_key` and `display` to input/output values from/to the user interface. 


## Testing
* done

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory
