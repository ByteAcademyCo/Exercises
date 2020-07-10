import json
def convert(dict):
    data=json.dumps(dict)
    return data
my_dict = {"students":[{"firstName": "Nikki", "lastName": "Roysden"},
               {"firstName": "Mervin", "lastName": "Friedland"},
               {"firstName": "Aron ", "lastName": "Wilkins"}],
"teachers":[{"firstName": "Amberly", "lastName": "Calico"},
         {"firstName": "Regine", "lastName": "Agtarap"}]}

result = convert(my_dict)
print(result)

