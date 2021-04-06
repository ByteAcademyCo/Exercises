import os

def test_solution():
    solution = {}
    for dir_name, subdir_list, file_list in os.walk("star_wars"):
        solution[dir_name] = set(file_list)
    if not solution.get("star_wars/tatooine"):
        solution.update({'star_wars/tatooine': set(), 'star_wars/the_empire': set()})
    assert solution == {'star_wars': set(), 
                        'star_wars/tatooine': set(), 
                        'star_wars/tie_fighter': {'darth_vader.txt'}, 
                        'star_wars/x_wing': {'luke_skywalker.txt'}, 
                        'star_wars/millenium_falcon': {'han_solo.txt', 'chewbacca.txt'}, 
                        'star_wars/the_rebellion': {'leia_organa.txt'}, 
                        'star_wars/the_empire': set()
                        }
