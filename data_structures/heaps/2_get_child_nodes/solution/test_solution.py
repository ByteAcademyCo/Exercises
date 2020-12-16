def test_solution():
  from solution import get_child_nodes
  assert get_child_nodes([2, 3, 4, 5, 10], 0) == [3, 4]
  assert get_child_nodes([2, 3, 4, 5, 10], 3) == []
  assert get_child_nodes([2, 3, 4, 5, 10, 11], 2) == [11]
  assert get_child_nodes([], 2) == []