def longest_common_subseq(str1, str2):
    # find the length of the strings 
    len1 = len(str1) 
    len2 = len(str2) 
  
    # memo will be a len2 by len1 matrix. memo[i][j] will
    # be used to store the length of the LCS of str1[0...i-1]
    # and str2[0...j-1]
    memo = [[None]*(len2 + 1) for i in range(len1 + 1)] 
  
    for i in range(len1 + 1): 
        for j in range(len2 + 1): 
            # if either i or j is 0, the LCS will be 0
            if i == 0 or j == 0 : 
                memo[i][j] = 0
            # if the ith element in str1 == the ith element in str2
            # the LCS will be 1+ the LCS of str1[0...i-2] and str2[0...j-2]
            # which we already stored in memo[i-1][j-1].
            elif str1[i-1] == str2[j-1]: 
                memo[i][j] = memo[i-1][j-1]+1
            else: 
                # otherwise the ith and jth elements are not equal
                # so the LCS will be the max of the LCS for
                # str1[0...i-2] and str2[0...j-1] OR 
                # str1[0...i-1] and str2[0...j-2]. 
                memo[i][j] = max(memo[i-1][j], memo[i][j-1]) 
  
    # memo[len1][len2] contains the length of LCS of str1[0..len1-1] & str2[0..len2-1] 
    return memo[len1][len2]