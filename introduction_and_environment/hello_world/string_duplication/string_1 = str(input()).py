string_1 = str(input())
dup_val = int(input())

data = string_1 * dup_val

data_2 = [i for r in data.split() for i in (r, f'\n')[:-1]]


print(data_2)