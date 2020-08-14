class Tree:
  def __init__(self, root_node=None):
      self.root_node = root_node

class TreeNode:
  def __init__(self, value, left=None, right=None):
      self.value = value
      self.left = left
      self.right = right

class MinHeap:
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
      if self._is_valid_index(parent_index) and self._heap[index] < self._heap[parent_index]:
          self._swap_nodes(index, parent_index)
          self._sift_up(parent_index)

# Fill in your code here
def convert_to_minHeap(tree):
  return