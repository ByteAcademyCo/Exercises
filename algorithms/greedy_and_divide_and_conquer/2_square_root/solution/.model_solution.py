def bin_sqrt(n):
    # Base cases 
    if (n == 0 or n == 1) : 
        return n
   
    # Do Binary Search for floor(sqrt(x)) 
    # we start a 1 and count up to end 
    start = 1
    end = n   
    while (start <= end) : 
        # calculate the mid point between start and end
        mid = (start + end) // 2
          
        # If n is a perfect square 
        if (mid*mid == n) : 
            return mid
              
        # update answer when mid*mid is smaller 
        # than n, and move closer to sqrt(n) 
        if (mid * mid < n) : 
            # update the starting point because the answer will
            # either be mid or somewhere between mid+1 and end.
            start = mid + 1
            ans = mid 
              
        else : 
            # If mid*mid is greater than n we update end
            # because the answer will be between start and mid-1
            end = mid-1
              
    return ans

print(bin_sqrt(120))