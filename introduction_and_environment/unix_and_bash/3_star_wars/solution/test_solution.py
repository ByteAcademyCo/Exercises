import os

def test_solution():
    solution = {}
    for dir_name, subdir_list, file_list in os.walk("star_wars"):
    # dir_name, subdir_list, file_list = os.walk(".")
        print(dir_name, subdir_list, file_list)
        solution[dir_name] = file_list

    assert solution == {'star_wars': [], 
                        'star_wars/tatooine': [], 
                        'star_wars/tie_fighter': ['darth_vader.txt'], 
                        'star_wars/x_wing': ['luke_skywalker.txt'], 
                        'star_wars/millenium_falcon': ['han_solo.txt', 'chewbacca.txt'], 
                        'star_wars/the_rebellion': ['leia_organa.txt'], 
                        'star_wars/the_empire': []
                        }
