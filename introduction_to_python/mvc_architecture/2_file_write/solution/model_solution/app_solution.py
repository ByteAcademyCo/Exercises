import model_solution as model
import view_solution as view

file_name = input(view.ask_fileName())
model.create(file_name)
content = input(view.ask_content())
model.write(file_name, content)
data = model.read(file_name)
result = view.display(data)
print(result)
