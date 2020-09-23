#  MVC File Write 

## Motivation
View is a user interface. View display data using model to the user and also enables them to modify the data.

Any representation of information such as a chart, diagram or table. Multiple views of the same information are possible, such as a bar chart for management and a tabular view for accountants.


## Problem Description
Construct a MVC to create,write to a text file name of your choice while having below conditions:

'model' create 3 functions `create` to create a new text file name of your choise,`write` to append contents and `read` to capture and return content. 

'app' containing logic related to the controller where objects `file_name` , `content` are used to capture file name from user and also capture content to write into the text file from view. Create object `data` which peforms a function call to model to read contents of the file and display the `result` object to the view. 

'view' containing functions `ask_filename`,`ask_content` and `display` to input/output values from/to the user interface. 


## Testing
* done

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory
