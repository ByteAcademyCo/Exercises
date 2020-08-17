# Write your solution here
def get_parent_node(heap, index):
    parent_index = (index-1) // 2      #parent of heap[i]
    if index == 0 and len(heap) > 0:
        return heap[0]                 # root is heap[0]
    elif index < len(heap):
        return heap[parent_index]
    return f'{index} is not a valid index in the heap'