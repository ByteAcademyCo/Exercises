import model_solution as model
import view_solution as view

program_list = model.get_list()
show = view.show_list(program_list)
print(show)
key = input(view.update_key())
value = input(view.enter_value())
model.update_list_key(key, value)
new_list = model.get_list()
result = view.display(new_list)
print(result)

# do()
