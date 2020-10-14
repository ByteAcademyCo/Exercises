def get_child_nodes(heap, index):
    left_idx = index*2 + 1
    right_idx = index*2 + 2
    child_lst = []
    if left_idx < len(heap):
        child_lst.append(heap[left_idx])
    if right_idx < len(heap):
        child_lst.append(heap[right_idx])
    return child_lst