import provided_code
provided_code.x = 20
provided_code.y = 10
import solution

def test_solution():
    assert solution.my_sum == 30
    assert solution.my_diff == 10
    assert solution.my_mult == 200
    assert solution.my_div == 2
    assert solution.my_power == 10240000000000
    assert solution.my_quotient == 2
    assert solution.my_remainder == 0
