import model_solution as model
import view_solution as view 

number_1=input(view.capture_number1())
number_2=input(view.capture_number2())
result=int(number_1)+int(number_2)
model.store([number_1,number_2,result])
print(view.display(result))


# do()