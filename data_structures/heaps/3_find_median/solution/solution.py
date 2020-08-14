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

  def pop_min(self):
      if not self._heap:
          raise IndexError("Tried to pop an empty MinHeap")
      self._swap_nodes(0, -1)
      min_value = self._heap.pop()
      self._sift_down(0)
      return min_value

  def _sift_down(self, index):
      left_child_index = 2*index + 1
      right_child_index = 2*index + 2
      if self._is_valid_index(right_child_index):
          if self._heap[left_child_index] < self._heap[right_child_index]:
              smallest_child_index = left_child_index
          else:
              smallest_child_index = right_child_index
      elif self._is_valid_index(left_child_index):
          smallest_child_index = left_child_index
      else:
          return
      if self._heap[smallest_child_index] < self._heap[index]:
          self._swap_nodes(smallest_child_index, index)
          self._sift_down(smallest_child_index)
      return

# Fill in your code here
def find_median(lst):
    return