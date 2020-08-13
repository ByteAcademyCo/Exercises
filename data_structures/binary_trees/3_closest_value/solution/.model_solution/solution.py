class Node:
    def __init__(self, key, left=None, right=None):
        self.left = left
        self.right = right
        self.key = key

def closest_value_helper(node, target, prev):
    if node:
        if node.key == target:
            return node.key
        child = node.left if node.key > target else node.right
        closest = closest_value_helper(child, target, node.key)
        if abs(closest - target) < abs(node.key - target):
            return closest
        else:
            return node.key
    return prev

def closest_value(node, target):
    return closest_value_helper(node, target, node.key)

root = Node(6)
root.left = Node(4)
root.right = Node(10)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(8)
root.right.right = Node(12)

print(closest_value(root, 9))