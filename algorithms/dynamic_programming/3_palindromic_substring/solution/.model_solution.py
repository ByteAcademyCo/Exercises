
def longest_palindrome_substr(str):
    n = len(str)
    if n == 0:
        return 0
  
    # table[i][j] will be True if substring  
    # str[i..j] is a palindrome and False otherwise
    table = [[0 for x in range(n)] for y in range(n)]  
      
    # All substrings of length 1 are palindromes 
    # set the maxLength we've seen so far to be 1.
    maxLength = 1
    for i in range(n): 
        table[i][i] = True
      
    # check for sub-strings of length 2. 
    start = 0
    for i in range(n-1): 
        if (str[i] == str[i + 1]) : 
            table[i][i + 1] = True
            start = i 
            maxLength = 2
      
    # Check for lengths greater than 2.  
    # k is length of substring 
    for k in range(3, n+1): 
        # Fix the starting index 
        for i in range(n - k + 1): 
              
            # Get the ending index of  
            # substring from starting  
            # index i and length k 
            j = i + k - 1
      
            # checking for sub-string from 
            # ith index to jth index iff  
            # str[i+1] to st[j-1] is a  
            # palindrome 
            if (table[i + 1][j - 1] and str[i] == str[j]) : 
                table[i][j] = True
                if (k > maxLength) : 
                    start = i 
                    maxLength = k 

    print("Longest palindrome substring is: " + str[start: start + maxLength]) 
  
    return maxLength # return length of LPS

print(longest_palindrome_substr("abaccad"))