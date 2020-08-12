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
stack3.push(2)

def test_solution():
    assert (stack1 == stack2) == False
    assert (stack2 == stack3) == True
    assert (stack3 == stack1) == False