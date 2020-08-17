def is_max_heap(heap):
    if len(heap) == 0:
        return True
    for i in range(len(heap)):
        root = heap[i]
        leftidx = (2*i) + 1 
        rightidx = (2*i) + 2
        left_child = None
        right_child = None
        if (2*i)+1 < len(heap):
            left_child = heap[(2*i)+1]
        if (2*i)+2 < len(heap):
            right_child = heap[(2*i)+2]
        if left_child == None and right_child == None:
            return True
        if left_child == None:
            if right_child < root:
                return is_max_heap(heap[rightidx:])
            elif right_child > root:
                return False
        if right_child == None:
            if left_child < root:
                return is_max_heap(heap[leftidx:])
            elif left_child > root:
                return False
        if left_child > root or right_child > root:
            return False
    return True

def is_min_heap(heap):
    if len(heap) == 0:
        return True
    for i in range(len(heap)):
        root = heap[i]
        leftidx = (2*i) + 1 
        rightidx = (2*i) + 2
        left_child = None
        right_child = None
        if (2*i)+1 < len(heap):
            left_child = heap[(2*i)+1]
        if (2*i)+2 < len(heap):
            right_child = heap[(2*i)+2]
        if left_child == None and right_child == None:
            return True
        if left_child == None:
            if right_child > root:
                return is_min_heap(heap[rightidx:])
            elif right_child < root:
                return False
        if right_child == None:
            if left_child > root:
                return is_min_heap(heap[leftidx:])
            elif left_child < root:
                return False
        if left_child < root or right_child < root:
            return False
    return True


def min_or_max_heap(heap):
    if is_min_heap(heap):
        return "min"
    elif is_max_heap(heap):
        return "max"
    else:
        return "neither"
    

print(min_or_max_heap([1, 3, 5, 7, 4, 8]))