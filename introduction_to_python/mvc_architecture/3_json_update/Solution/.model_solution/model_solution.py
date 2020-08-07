import json 
match_data={"sports":["Football","Soccer","Tennis","Cricket","Basketball"],"country":["Switzerland","India","Brazil","USA","Spain"]}
data_match=json.dumps(match_data)

def get_list():
    return data_match

def retrive_match(sport,country):
    data=json.loads(data_match)
    # result=data["sports"].get(sport)
    sport_list=data["sports"]
    sport_list.append(sport)
    country_list=data["country"]
    country_list.append(country)
    return data
# print(retrive_match("abc","xzy"))




    # sport_a= idx for idx in data["sports"] 
    # counry_a=data["country"].get(country)

    # return sport_a,counry_a
#     for key, value in result:
#         if book in key:
#             item=value[book]
#             retrive_author(item)
#             return value[book]
#         else:
#             break 

# retrive_book("Lord Of The Rings")



    
    

