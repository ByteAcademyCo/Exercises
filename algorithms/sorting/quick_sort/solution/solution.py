def median_of_medians(lst):
    # Split our list into sublists len 5. (The last list may have < 5 elements)    
    sublists = [lst[j:j+5] for j in range(0, len(lst), 5)]
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

def _partition(lst, min_index, max_index):
    # get pivot index using the median of medians algorithm.
    pivot_index = lst.index(median_of_medians(lst[min_index:max_index+1]))
    # swap the position of the first element in lst and the pivot element
    lst[min_index], lst[pivot_index] = lst[pivot_index], lst[min_index]
    # swap the indices, pivot index is now at the front of the list.
    pivot_index = min_index
    # itterate through min_index to max_index+1
    for index in range(min_index, max_index + 1):
        # if elem at index is less than pivot
        if lst[index] < lst[pivot_index]:
            # swap the position elem and pivot. 
            lst[pivot_index], lst[index] = lst[index], lst[pivot_index]
            # move pivot to next position in the list swapping next element with pivot element.
            lst[pivot_index + 1], lst[index] = lst[index], lst[pivot_index + 1]
            # update pivot index.
            pivot_index += 1
    return pivot_index

def quick_sort_helper(lst, min_index, max_index):
    if min_index < max_index:
        # find the pivot index partitioning list of all elems
        # less than median pivot and all elems greater than pivot
        pivot_index = _partition(lst, min_index, max_index)
        # recurse on list of elems smaller than pivot
        quick_sort_helper(lst, min_index, pivot_index - 1)
        # recurse on list of elems greater than pivot
        quick_sort_helper(lst, pivot_index + 1, max_index)

def quick_sort(lst):
    quick_sort_helper(lst, 0, len(lst) - 1)
    return lst
