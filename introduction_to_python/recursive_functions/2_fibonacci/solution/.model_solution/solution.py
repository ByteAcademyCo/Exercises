def fibonacci(n):
    def helper(n, counter=1, previous=1, second_previous=1):
        if counter == n:
            return second_previous
        else:
            return helper(n, counter+1, previous+second_previous, previous)

    return helper(n)

