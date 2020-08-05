class py_solution:
   def is_valid_parenthese(self, str):
      stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
      for parentheses in str:
         if parentheses in pchar:
            stack.append(parentheses)
         elif len(stack) == 0 or pchar[stack.pop()] != parentheses:
            return False
      return len(stack) == 0