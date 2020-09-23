class Node:
    def __init__(self, key, left=None, right=None):
        self.left = left
        self.right = right
        self.key = key

def closest_value_node(node, target, prev):
    if node:
        if node.key == target:
            return node.key
        child = node.left if target < node.key else node.right
        closest_child_val = closest_value_node(child, target, node.key)
        if abs(target - node.key) < abs(target - closest_child_val):
            node.key
        else:
            return closest_child_val
    return prev

def closest_value(node, target):
    return closest_value_node(node, target, node.key)

root = Node(6)
root.left = Node(4)
root.right = Node(10)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(8)
root.right.right = Node(12)

print(closest_value(root, 12))

def closest_value2(root, target):
    a = root.key
    kid = root.left if target < a else root.right
    if not kid:
        return a
    b = closest_value(kid, target)
    return min((a,b), key=lambda x: abs(target-x))