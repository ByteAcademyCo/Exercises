def longest_common_subseq(str1, str2):
    # find the length of the strings 
    len1 = len(str1) 
    len2 = len(str2) 
  
    # declaring the array for storing the dp values 
    L = [[None]*(len2 + 1) for i in range(len1 + 1)] 
  
    #Following steps build L[len1 + 1][len2 + 1] in bottom up fashion 
    #Note: L[i][j] contains length of LCS of str1[0..i-1] 
    #and str2[0..j-1]
    for i in range(len1 + 1): 
        for j in range(len2 + 1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif str1[i-1] == str2[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j], L[i][j-1]) 
  
    # L[len1][len2] contains the length of LCS of X[0..n-1] & Y[0..m-1] 
    return L[len1][len2]
print(longest_common_subseq("abcdabcf", "ecfdacagb")) 