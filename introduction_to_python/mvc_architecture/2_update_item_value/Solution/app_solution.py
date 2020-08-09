import model_solution as model
import view_solution as view 

program_list = model.get_list
key = input(view.update_key())
value = input(view.enter_value())
new_list = model.update_list_key(key, value)
result = view.display(new_list)
print(result)