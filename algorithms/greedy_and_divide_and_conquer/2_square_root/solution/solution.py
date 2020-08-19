def bin_sqrt(n):
    if n == 0 or n == 1:
        return n
    beginning = 1
    end = n
    while beginning <= end:
        mid = (beginning + end) // 2
        if mid*mid == n:
            return mid
        if mid*mid < n:
            beginning = mid + 1
            answer = mid
        else:
            end = mid - 1
    return answer