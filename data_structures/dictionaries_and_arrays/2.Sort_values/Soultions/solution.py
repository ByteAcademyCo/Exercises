import operator
my_dict = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
results = dict(sorted(my_dict.items(), key=operator.itemgetter(1)))
print('Dictionary in ascending order by value : ',results)
results = dict(sorted(my_dict.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',results)