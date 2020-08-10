# Write your solution here
import operator
def sort_dict(my_dictionary):
    return dict(sorted(my_dictionary.items(), key = operator.itemgetter(1)))