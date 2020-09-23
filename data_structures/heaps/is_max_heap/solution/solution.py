def is_max_heap(lst):
    if len(lst) == 0:
        return True
    for i in range(len(lst)):
        root = lst[i]
        leftidx = (2*i) + 1 
        rightidx = (2*i) + 2
        left_child = None
        right_child = None
        if (2*i)+1 < len(lst):
            left_child = lst[(2*i)+1]
        if (2*i)+2 < len(lst):
            right_child = lst[(2*i)+2]
        if left_child == None and right_child == None:
            return True
        if left_child == None:
            if right_child < root:
                return is_max_heap(lst[rightidx:])
            elif right_child > root:
                return False
        if right_child == None:
            if left_child < root:
                return is_max_heap(lst[leftidx:])
            elif left_child > root:
                return False
        if left_child > root or right_child > root:
            return False
    return True