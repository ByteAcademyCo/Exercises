#  MVC Books

## Motivation
View is a user interface. View display data using model to the user and also enables them to modify the data.

Any representation of information such as a chart, diagram or table. Multiple views of the same information are possible, such as a bar chart for management and a tabular view for accountants.


## Problem Description
Construct a MVC to return the author name for a book from a json data of book author matches in key value pairs while having below conditions:

'model' create a dict object `book_author_list` containing different book authors, convert into a json object `book_list`.
Create 2 functions `get_list` to return book author data and `retrive_book` to return specific book and author.

'app' containing logic related to the controller where objects `book_list` , `book` are used to capture list from model and ask user to enter book name after displaying list book from object `show` which outputs the list of book authors . Create object `author` which peforms a function call to model to retrive the author name for the book inputed and finnaly display the `data` object containing book and author to the view. 

'view' containing functions `show_list`,`retrive_book` and `display` to input/output values from/to the user interface. 


## Testing
* done

## Submission
* Submit your answers in the *solution.py* file within the *Solutions* subdirectory within this directory
