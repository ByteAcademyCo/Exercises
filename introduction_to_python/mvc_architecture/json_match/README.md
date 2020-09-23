#  MVC Json Match 

## Motivation
The controller is responsible for responding to the user input and perform interactions on the data model objects. The controller receives the input, it validates the input and then performs the business operation that modifies the state of the data model.
Accepts input and converts it to commands for the model or view.


## Problem Description
Construct a MVC to return the sport and country match of your choice from am existing user defined json data containing list of sports and list of country while having below conditions. 

'model' create a dict object `match_data` containing list of sports and list of country, convert into a json object `data_match`.
Create 2 functions `get_list` to return data and `retrive_match` to return specific sport and country.

'app' containing logic related to the controller where objects `data_list`  to capture list from model and display with object `show`.Capture user input in objects `sport` and `country` from view. Create objects `data_a` and `data_b` which peforms a function call to model to retrive sport and country ,finnaly diplay the `result` object to the view. 

'view' containing functions `show_list`,`retrive_sport`,`retrive_country` and `display` to input/output values from/to the user interface. 


## Testing
* done

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory
