movie_list={'1':'World War Z','2':'Inception','3':'Black Mirror','4':'Once Upon A Time In Hollywood','5':'Birdman'}

def get_list():
    return str(movie_list)

def del_list_key(del_key):
    del movie_list[del_key]