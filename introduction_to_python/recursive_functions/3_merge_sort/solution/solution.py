# Write your solution here
def custom_sort(num_list):
    if len(num_list)>1:
        mid = len(num_list) // 2
        left = num_list[:mid]
        right = num_list[mid:]
        custom_sort(left)
        custom_sort(right)
        a = b = c = 0

        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                num_list[c] = left[a]
                a += 1
                c += 1
            else:
                num_list[c] = right[b]
                b += 1
                c += 1
        while a < len(left):
            num_list[c] = left[a]
            a += 1
            c += 1
        while b < len(right):
            num_list[c] = right[b]
            b += 1
            c += 1
    return num_list