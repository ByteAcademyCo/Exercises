#Write your solutions here
class Node:
    def __init__(self, key, left=None, right=None):
        self.left = left
        self.right = right
        self.key = key

# def closest_value_helper(node, target, previous):
#     if node:
#         if node.key == target:
#             return node.key
#         child = node.left if target < node.key else node.right
#         closest_child = closest_value_helper(child, target, node.key)
#         if abs(target - node.key) < abs(target - closest_child):
#             return node.key
#         else:
#             return closest_child
#     return previous

# def closest_value(node, target):
#     return closest_value_helper(node, target, node.key)

def closest_value(node, target):
    a = node.key
    if target < a:
        child = node.left
    else:
        child = node.right
    if not child:
        return a
    b = closest_value(child, target)
    return min((a,b), key=lambda x: abs(target - b))