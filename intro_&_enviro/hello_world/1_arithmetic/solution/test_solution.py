import provided_code
provided_code.x = 20
provided_code.y = 10
import solution

def test_solution():
    assert solution.SUM == 30
    assert solution.DIFF == 10
    assert solution.MULT == 200
    assert solution.DIV == 2
    assert solution.QUOTIENT == 2
    assert solution.REMAINDER == 0
