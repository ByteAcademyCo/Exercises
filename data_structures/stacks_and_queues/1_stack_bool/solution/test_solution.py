import solution

stack1 = solution.Stack()
stack1.push(1)
stack1.push(2)

stack2 = solution.Stack()


def test_solution():
    assert bool(stack1) == True
    assert bool(stack2) == False