import model_solution as model
import view_solution as view 

movie_list=model.get_list()
print(view.display(movie_list))
del_key=input(view.delete_key())
model.del_list_key(del_key)
final_list=model.get_list()
print(view.display(final_list))

# do()