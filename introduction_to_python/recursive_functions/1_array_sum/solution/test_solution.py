def test_solution(monkeypatch):
    from solution import sum_array

    assert sum_array(num_list=[1, 2, 3]) == 6
    assert sum_array(num_list=[1, -2, 3.5]) == 2.5
    assert sum_array(num_list=[]) == 0
