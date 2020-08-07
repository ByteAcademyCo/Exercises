import view_solution as view
import model_solution as model

model.create()
result=model.query()
for i in range(len(result)):
    data=view.display(result[i][0],result[i][1])
    print(data)


# do()