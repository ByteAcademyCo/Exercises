import solution

def test_solution(monkeypatch):
    assert solution.sum_array(num_list=[1,2,3]) == 6
    assert solution.sum_array(num_list=[1,-2,3.5]) == 2.5
    assert solution.sum_array(num_list=[]) == 0

