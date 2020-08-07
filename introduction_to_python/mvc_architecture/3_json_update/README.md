#  MVC Json Update

## Motivation
Because MVC decouples the various components of an application, developers are able to work in parallel on different components without affecting or blocking one another. 

For example, a team might divide their developers between the front-end and the back-end. The back-end developers can design the structure of the data and how the user interacts with it without requiring the user interface to be completed. Conversely, the front-end developers are able to design and test the layout of the application prior to the data structure being available.



## Problem Description
Construct a MVC to add a new sport and country match of your choice to an existing json data containing list of sports and list of country while having below conditions. 

'model' create a dict object `match_data` containing list of sports and list of country, convert into a json object `data_match`.
Create 2 functions `get_list` to return data and `retrive_match` to return list of sport and country after appending. 

'app' containing logic related to the controller where objects `data_list`  to capture list from model and display with object `show`.Capture user input in objects `sport` and `country` from view. Create object `data_a`  which peforms a function call to model to perform updation of original list of sport and country ,finnaly diaplay the `result` object to the view. 

'view' containing functions `show_list`,`retrive_sport`,`retrive_country` and `display` to input/output values from/to the user interface. 


## Testing
* done

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory
