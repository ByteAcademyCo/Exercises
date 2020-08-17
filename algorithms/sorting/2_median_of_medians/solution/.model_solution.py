def median_of_medians(lst):
    #Split our list into sublists len 5. (The last list may have < 5 elements)    
    sublists = [lst[j:j+5] for j in range(0, len(lst), 5)]
    print(sublists)
    #Find medians in all sublists
    medians = []
    for sublist in sublists:
        medians.append(sorted(sublist)[len(sublist)//2])
        print(medians)
    if len(medians) <= 5:
        return sorted(medians)[len(medians)//2]
    else:
        return median_of_medians(medians)

print(median_of_medians([9, 1, 0, 2, 3, 4, 6, 8, 7, 10, 5]))

