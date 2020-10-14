def median_of_medians(lst):
    # Split our list into sublists len 5. (The last list may have < 5 elements)    
    sublists = [lst[j:j+5] for j in range(0, len(lst), 5)]
    print(f'sublists: {sublists}')
    # create list medians to store medians in all sublists
    medians = []
    for sublist in sublists:
        # append the median of each sublist to our medians list
        medians.append(sorted(sublist)[len(sublist)//2])
    # if we have <= 5 medians we get the middle element in our medians list.
    if len(medians) <= 5:
        return sorted(medians)[len(medians)//2]
    # if we have more than 5 medians, we recurse on our medians list
    else:
        return median_of_medians(medians)