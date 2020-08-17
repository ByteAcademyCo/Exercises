program_list={'1':'Perl','2':'C','3':'C++','4':'Java','5':'Python'}

def get_list():
    return str(program_list)

def update_list_key(key,value):
    for key, value in enumerate(program_list):
        return key, value