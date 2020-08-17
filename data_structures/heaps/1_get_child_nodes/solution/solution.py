# Write your solution here
def get_child_nodes(heap, index):
    left_index = 2*index + 1       #left child of heap[i] 
    right_index = 2*index + 2      #right child of heap[i]
    lst = []                       #creating empty list to append index's of heap
    if left_index < len(heap):
        lst.append(heap[left_index])
    if right_index < len(heap):
        lst.append(heap[right_index])
    return lst