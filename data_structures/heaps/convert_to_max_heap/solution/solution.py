class Tree:
  def __init__(self, root_node=None):
      self.root_node = root_node

class TreeNode:
  def __init__(self, value, left=None, right=None):
      self.value = value
      self.left = left
      self.right = right

class MaxHeap:
  def __init__(self):
      self._heap = []

  def __str__(self):
      return str(self._heap)

  def _is_valid_index(self, index):
      if 0 <= index and index < len(self._heap):
          return True
      return False

  def _swap_nodes(self, index1, index2):
      self._heap[index1], self._heap[index2] = self._heap[index2], self._heap[index1]

  def push(self, value):
      self._heap.append(value)
      self._sift_up(len(self._heap) - 1)
      
  def _sift_up(self, index):
      parent_index = (index-1) // 2
      if self._is_valid_index(parent_index) and self._heap[index] > self._heap[parent_index]:
          self._swap_nodes(index, parent_index)
          self._sift_up(parent_index)


def convert_to_array_nodes(treeNode):
  if not treeNode:
    return []
  return [treeNode.value] + convert_to_array_nodes(treeNode.left) + convert_to_array_nodes(treeNode.right)

def convert_to_maxHeap(tree):
  mheap = MaxHeap()
  if not tree:
    return mheap
  nodeList = convert_to_array_nodes(tree.root_node)
  for n in nodeList:
    mheap.push(n)
  return mheap


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3, n1, n2)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6, n4, n5)
n7 = TreeNode(7, n3, n6)
tree = Tree(n7)

print(convert_to_maxHeap(tree))
  