class Node:
    def __init__(self, key, left=None, right=None):
        self.left = left
        self.right = right
        self.key = key


left_child = Node(6, None, None)
right_child = Node(7, None, None)
sample_tree = Node(5, left_child, right_child)


print(f'key is: {sample_tree.key}')
print(f'left child is: {sample_tree.left.key}')
print(f'right child is: {sample_tree.right.key}')




