def get_parent_node(heap, index):
    parent_idx = (index-1)//2
    if index == 0 and len(heap)>0:
        return heap[0]
    if index<len(heap):
        return heap[parent_idx]
    else: 
        return f'{index} is not a valid index in the heap'
