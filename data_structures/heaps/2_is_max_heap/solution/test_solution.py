def test_solution():
  from solution import is_max_heap
  assert is_max_heap([1, 2, 3, 7, 6, 4, 5]) == False
  assert is_max_heap([1]) == True
  assert is_max_heap([2,1]) == True
  assert is_max_heap([6, 5, 4, 3, 1, 2]) == True
  assert is_max_heap([]) == True
