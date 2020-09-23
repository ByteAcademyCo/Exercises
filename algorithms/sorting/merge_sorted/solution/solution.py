def merge_sorted(lst1, lst2):
    def merge_helper(lst1, lst2, merged_lst):
        # if list1 has no elements we add lst2 to the 
        # end of our merged_lst
        if len(lst1) == 0:
            merged_lst.extend(lst2)
            return merged_lst
        # if list2 has no elements we add lst1 to the 
        # end of our merged_lst
        elif len(lst2) == 0:
            merged_lst.extend(lst1)
            return merged_lst
        # if first element of lst1 <= first element of lst2
        elif lst1[0] <= lst2[0]:
            # we add that element to our merged list
            merged_lst.append(lst1[0])
            # and we recurse on the rest of lst1, keeping lst2 unchanged
            return merge_helper(lst1[1:], lst2, merged_lst)
        else:
            # the first element of lst2 < first element of lst1
            # so we add that element to our merged list
            merged_lst.append(lst2[0])
            # and we recurse on the rest of lst2, keeping lst1 unchanged
            return  merge_helper(lst1, lst2[1:], merged_lst)
    return merge_helper(lst1, lst2, [])