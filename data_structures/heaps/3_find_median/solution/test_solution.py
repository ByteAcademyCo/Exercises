def test_solution():
  from solution import find_median
  assert find_median([1, 2, 3, 7, 6, 4, 5]) == 4
  assert find_median([1]) == 1
  assert find_median([1,2]) == 2