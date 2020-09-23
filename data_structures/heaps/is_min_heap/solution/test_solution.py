def test_solution():
  from solution import is_min_heap
  assert is_min_heap([1, 2, 3, 7, 6, 4, 5]) == True
  assert is_min_heap([1]) == True
  assert is_min_heap([2,1]) == False
  assert is_min_heap([6, 5, 4, 7, 9]) == False
  assert is_min_heap([]) == True
