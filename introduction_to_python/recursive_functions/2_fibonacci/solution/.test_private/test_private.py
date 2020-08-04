from sys import path
path.append('..')

import pytest
import pytest_dependency
import solution
import time


def test_invalid_input():
    assert solution.fibonacci(n=0) == -1
    assert solution.fibonacci(n=-10) == -1


@pytest.mark.dependency()
def test_efficiency():
    start = time.time()
    solution.fibonacci(37)
    efficiency = time.time() - start
    assert efficiency < 0.001


@pytest.mark.xfail(raises=RecursionError, reason='not allowed to use iteration')
@pytest.mark.dependency(depends=['test_efficiency'])
def test_iterative_solution():
    assert solution.fibonacci(10000)

