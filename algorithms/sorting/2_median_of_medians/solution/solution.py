def median_of_medians(lst):
    sublists = [lst[i:i+5] for i in range(0, len(lst), 5)]
    medians = []
    for lists in sublists:
        medians.append(sorted(lists)[len(lists)//2])
    if len(medians) <= 5:
        return sorted(medians)[len(medians)//2]
    else:
        return median_of_medians(medians)