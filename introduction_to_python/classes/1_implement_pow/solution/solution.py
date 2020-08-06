class py_solution:
   def pow(self, x, n):  
      if x == 0:
        return 0
      elif n == 0:
        return 1
      else:
        return x*pow(x, n-1)