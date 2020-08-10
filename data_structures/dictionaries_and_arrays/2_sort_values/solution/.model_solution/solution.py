def sort_dict(my_dictionary):
    import operator

    results = dict(sorted(my_dict.items(), key=operator.itemgetter(1)))
    return results
