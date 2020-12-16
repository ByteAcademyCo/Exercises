def test_solution():
  from solution import find_kth_largest
  assert find_kth_largest([1, 2, 7, 6, 4], 2) == 6
  assert find_kth_largest([1, 2], 2) == 1
  assert find_kth_largest([7, 1, 2, 9], 1) == 9