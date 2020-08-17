import model_solution as model
import view_solution as view 

book_list = model.get_list()
show = view.show_list(book_list)
print(show)
book = input(view.retrive_book())
author = model.retrive_book(book)
data = view.display(book, author)
print(data)