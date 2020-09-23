#  MVC Sqlite Connection 

## Motivation
Advantages of MVC -

Simultaneous development – Multiple developers can work simultaneously on the model, controller and views.
High cohesion – MVC enables logical grouping of related actions on a controller together. The views for a specific model are also grouped together.
Loose coupling – The very nature of the MVC framework is such that there is low coupling among models, views or controllers. 
Ease of modification – Because of the separation of responsibilities, future development or modification is easier
Multiple views for a model – Models can have multiple views


## Problem Description
Construct a MVC to create a new sqlite database connection, create a table student , insert values and display data while having below conditions. 

'model' create 2 functions `create` to set up sqlite connction,create cursor connection to execute create table student query and `query` to insert values into the table student and return result set. 

'app' containing logic related to the controller where object `result` to capture data from model and display. Create object `data` which perform function call to diplay the data to the view.

'view' containing function `display` to output values to the user interface. 


## Testing
* done

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory
