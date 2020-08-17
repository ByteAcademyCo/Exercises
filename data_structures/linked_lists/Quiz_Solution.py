#Quiz - 2

#Question1
class Tree:
    def __init__(self, root_node=None):
        self.root_node = root_node
        
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

items = Node(4)
items.left = Node(2)
items.right = Node(6)
items.left.left = Node(1)
items.left.right = Node(3)
items.right.left = Node(5)
items.right.right = Node(7)
my_tree_node = TreeNode(items)
# my_tree_node = TreeNode(items, items.left, items.right, items.left.left, items.left.right, items.right.left, items.right.right)

#Question2
class LinkedList:
    def __init__(self, head_node=None):
        self.head_node = head_node
    def remove_tail(self):
        if self.head_node is None:
            return None
        n = self.head_node
        while n.next.next != None:
            n = n.next
        n.next = None

class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next