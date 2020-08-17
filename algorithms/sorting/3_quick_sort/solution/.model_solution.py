def median_of_medians(lst):
    #Split our list into sublists len 5. (The last list may have < 5 elements)    
    sublists = [lst[j:j+5] for j in range(0, len(lst), 5)]
    #Find medians in all sublists
    medians = []
    for sublist in sublists:
        medians.append(sorted(sublist)[len(sublist)//2])
    if len(medians) <= 5:
        return sorted(medians)[len(medians)//2]
    else:
        return median_of_medians(medians)


def _partition(lst, min_index, max_index):
    pivot_index = lst.index(median_of_medians(lst[min_index:max_index+1]))
    lst[min_index], lst[pivot_index] = lst[pivot_index], lst[min_index]
    pivot_index = min_index
    for index in range(min_index, max_index + 1):
        if lst[index] < lst[pivot_index]:
            lst[pivot_index], lst[index] = lst[index], lst[pivot_index]
            lst[pivot_index + 1], lst[index] = lst[index], lst[pivot_index + 1]
            pivot_index += 1
    return pivot_index

def quick_sort_helper(lst, min_index, max_index):
    if min_index < max_index:
        pivot_index = _partition(lst, min_index, max_index)
        quick_sort_helper(lst, min_index, pivot_index - 1)
        quick_sort_helper(lst, pivot_index + 1, max_index)

def quick_sort(lst):
    quick_sort_helper(lst, 0, len(lst) - 1)
    return lst



lst = [9, 1, 0, 2, 3, 4, 6, 8, 7, 10, 5]
print(quick_sort(lst))
#print(lst)