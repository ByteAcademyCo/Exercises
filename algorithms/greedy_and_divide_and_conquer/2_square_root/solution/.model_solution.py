def bin_sqrt(n):
    # Base cases 

    if (n == 0 or n == 1) : 
        return n
   
    # Do Binary Search for floor(sqrt(x)) 
    start = 1
    end = n   
    while (start <= end) : 
        mid = (start + end) // 2
          
        # If n is a perfect square 
        if (mid*mid == n) : 
            return mid
              
        # update answer when mid*mid is smaller 
        # than n, and move closer to sqrt(n) 
        if (mid * mid < n) : 
            start = mid + 1
            ans = mid 
              
        else : 
              
            # If mid*mid is greater than n 
            end = mid-1
              
    return ans

print(bin_sqrt(120))