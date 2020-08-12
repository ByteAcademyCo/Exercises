import solution

stack1 = solution.Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
stack1.push(5)

stack2 = solution.Stack()
stack2.push(2)

stack3 = solution.Stack()

def test_solution():
    assert len(stack1) == 5
    assert len(stack2) == 1
    assert len(stack3) == 0