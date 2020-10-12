import json

match_data = {
    "sports": ["Football", "Soccer", "Tennis", "Cricket", "Basketball"],
    "country": ["Switzerland", "India", "Brazil", "USA", "Spain"],
}
data_match = json.dumps(match_data)


def get_list():
    return data_match


def retrive_match(sport, country):
    data = json.loads(data_match)
    # result=data["sports"].get(sport)
    sport_list = data["sports"]
    if sport in sport_list:
        data_a = sport
        country_list = data["country"]
    if country in country_list:
        data_b = country
        return data_a, data_b
