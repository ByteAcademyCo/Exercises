import json 
match_data={"sports":["Football","Soccer","Tennis","Cricket","Basketball"],"country":["Switzerland","India","Brazil","USA","Spain"]}
data_match=json.dumps(match_data)

def get_list():
    return str(data_match)

def retrive_match(sport,country):
    x = json.loads(data_match)
    sport_lst=x['sports']
    sport_lst.append(sport)
    country_lst=x['country']
    country_lst.append(country)
    return x