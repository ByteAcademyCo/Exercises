def merge_sorted(lst1, lst2):
    def merge_helper(lst1, lst2, merged_lst):
        if len(lst1) == 0:
            merged_lst.extend(lst2)
            return merged_lst
        elif len(lst2) == 0:
            merged_lst.extend(lst1)
            return merged_lst
        elif lst1[0] <= lst2[0]:
            merged_lst.append(lst1[0])
            return merge_helper(lst1[1:], lst2, merged_lst)
        else:
            merged_lst.append(lst2[0])
            return  merge_helper(lst1, lst2[1:], merged_lst)
    return merge_helper(lst1, lst2, [])
