import view_solution as view
import model_solution as model

fruits = model.get_store()
show = view.show_fruits(fruits)
print(show)
fruit = input(view.ask_fruit())
model.update_fruit(fruit)
data = view.show_fruits(fruits)
print(data)

# do()
