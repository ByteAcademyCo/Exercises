def is_max_heap(heap):
    # if no elemts in the heap, it is by definition a max_heap
    # so we return true.
    if len(heap) == 0:
        return True
    # we itterate through the heap
    for i in range(len(heap)):
        # get value of the root element
        root = heap[i]
        # get the left and right child indices in the heap
        leftidx = (2*i) + 1 
        rightidx = (2*i) + 2
        # initialise left and right child variables to None
        left_child = None
        right_child = None
        # if leftidx is valid index in the heap we set the leftchild value
        if leftidx < len(heap):
            left_child = heap[leftidx]
        # if leftidx is valid index in the heap we set the leftchild value
        if rightidx < len(heap):
            right_child = heap[rightidx]
        # if both children are None, heap is a max_heap
        if left_child == None and right_child == None:
            return True
        # if we have no left child we only need to check the right side of 
        # the tree.
        if left_child == None:
            # if right child is less than root we recurse on the right side of the heap
            if right_child < root:
                return is_max_heap(heap[rightidx:])
            # if right child is greater than root it is not max_heap
            elif right_child > root:
                return False
        # if we have no right child we only need to check the left side of 
        # the tree.
        if right_child == None:
            # if left child is less than root we recurse on the left side of the heap
            if left_child < root:
                return is_max_heap(heap[leftidx:])
            # if left child is greater than root it is not max_heap
            elif left_child > root:
                return False
        # if either left or right is greater than the root it is not max_heap
        if left_child > root or right_child > root:
            return False
    return True

def is_min_heap(heap):
    # if no elemts in the heap, it is by definition a min_heap
    # so we return true.
    if len(heap) == 0:
        return True
    # we itterate through the heap
    for i in range(len(heap)):
        # get value of the root element
        root = heap[i]
        # get the left and right child indices in the heap
        leftidx = (2*i) + 1 
        rightidx = (2*i) + 2
        # initialise left and right child variables to None
        left_child = None
        right_child = None
        # if leftidx is valid index in the heap we set the leftchild value
        if leftidx < len(heap):
            left_child = heap[leftidx]
        # if leftidx is valid index in the heap we set the leftchild value
        if rightidx < len(heap):
            right_child = heap[rightidx]
        # if both children are None, heap is a min_heap
        if left_child == None and right_child == None:
            return True
        # if we have no left child we only need to check the right side of 
        # the tree.
        if left_child == None:
            # if right child is greater than root we recurse on the right side of the heap
            if right_child > root:
                return is_min_heap(heap[rightidx:])
            # if right child is less than root it is not min_heap
            elif right_child < root:
                return False
        # if we have no right child we only need to check the left side of 
        # the tree.
        if right_child == None:
            # if left child is greater than root we recurse on the left side of the heap
            if left_child > root:
                return is_min_heap(heap[leftidx:])
            # if left child is less than root it is not min_heap
            elif left_child < root:
                return False
        # if either left or right is less than the root it is not min_heap
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