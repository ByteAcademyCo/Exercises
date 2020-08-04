def count_down_from(num):
    if num >= 1:
        print(num)
        count_down_from(num-1)
