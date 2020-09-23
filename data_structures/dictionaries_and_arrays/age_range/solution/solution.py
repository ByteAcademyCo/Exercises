def remove_ages(pdict, x, y):
    ret_dict = {}
    for p, age in pdict.items():
        if age >= x and age <= y:
            ret_dict[p] = age
    return ret_dict