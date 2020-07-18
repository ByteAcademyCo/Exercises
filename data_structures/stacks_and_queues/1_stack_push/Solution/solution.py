# Code your solution here
from typing import Any


class Stack(list):
    def push(self, value: Any) -> Stack:
        self.append(value)
        return self

stack_a = Stack(['C','Perl','C++','Java'])
result = stack_a.push('Python')
print(result)
