#Write your solutions here
class Node:
    def __init__(self, key, left=None, right=None):
        self.left = left
        self.right = right
        self.key = key


def closest_value(node, target):
    a = node.key
    child = node.left if target < a else node.right