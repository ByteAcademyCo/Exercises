def longest_palindrome_substr(str):
    n = len(str)
    if n == 0:
        return 0
    table = [[0 for x in range(n)] for y in range(n)]
    max_length = 1
    for i in range(n):
        table[i][i] = True
    start = 0
    for i in range(n-1):
        if (str[i] == str[i+1]):
            table[i][i+1] = True
            start = i
            max_length = 2
        for k in range(3, n+1):
            for i in range(n - k + 1):
                j = i + k - 1
                if (table[i+1][j-1] and str[i] == str[j]):
                    table[i][j] = True
                    if k > max_length:
                        start = i
                        max_length = k
    return max_length