import model_solution as model
import view_solution as view 


data_list=model.get_list()
show=view.show_list(data_list)
print(show)
sport=input(view.retrive_sport())
country=input(view.retrive_country())
data_a,data_b=model.retrive_match(sport,country)
result=view.display(data_a,data_b)
print(result)

# do()