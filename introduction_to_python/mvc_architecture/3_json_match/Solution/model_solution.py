import json 
match_data={"sports":["Football","Soccer","Tennis","Cricket","Basketball"],"country":["Switzerland","India","Brazil","USA","Spain"]}
data_match=json.dumps(match_data)

def get_list():
    return str(data_match)

def retrive_match(sport,country):
    x = json.loads(data_match)
    sport_country = x['sport', 'country']
    result = sport_country.get(sport, country)
    return result 