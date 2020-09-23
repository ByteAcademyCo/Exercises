def test_solution():
  from solution import get_parent_node
  assert get_parent_node([2,3,4,5,10], 4) == 3
  assert get_parent_node([2,3,4,5,10], 0) == 2
  assert get_parent_node([2,3,4,5,10], 5) == "5 is not a valid index in the heap"
  assert get_parent_node([], 0) == "0 is not a valid index in the heap"
