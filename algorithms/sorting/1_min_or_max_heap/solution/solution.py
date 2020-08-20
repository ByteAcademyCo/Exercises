def max_heap(heap):
    if len(heap) == 0:
        return True
    for i in range(len(heap)):
        root = heap[i]
        leftindex = (2*i) + 1 
        rightindex = (2*i) + 2
        left = None
        right = None
        if (2*i)+1 < len(heap):
            left = heap[(2*i)+1]
        if (2*i)+2 < len(heap):
            right = heap[(2*i)+2]
        if left == None and right == None:
            return True
        if left == None:
            if right < root:
                return max_heap(heap[rightindex:])
            elif right > root:
                return False
        if right == None:
            if left < root:
                return max_heap(heap[leftindex:])
            elif left > root:
                return False
        if left > root or right > root:
            return False
    return True
def min_heap(heap):
    if len(heap) == 0:
        return True
    for i in range(len(heap)):
        root = heap[i]
        leftindex = (2*i) + 1 
        rightindex = (2*i) + 2
        left = None
        right = None
        if (2*i)+1 < len(heap):
            left = heap[(2*i)+1]
        if (2*i)+2 < len(heap):
            right = heap[(2*i)+2]
        if left == None and right == None:
            return True
        if left == None:
            if right > root:
                return min_heap(heap[rightindex:])
            elif right < root:
                return False
        if right == None:
            if left > root:
                return min_heap(heap[leftindex:])
            elif left < root:
                return False
        if left < root or right < root:
            return False
    return True
def min_or_max_heap(heap):
    if min_heap(heap):
        return 'min'
    elif max_heap(heap):
        return 'max'
    else:
        return 'neither'