def merge_sort(numbers: list) -> list:
    if len(numbers) < 2:
        return numbers

    middle_index = len(numbers) // 2
    left_half = numbers[:middle_index]
    right_half = numbers[middle_index:]

    return _merge(merge_sort(left_half), merge_sort(right_half))


def _merge(left: list, right: list) -> list:
    merged_list = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged_list.append(left[left_index])
            left_index += 1
        else:
            merged_list.append(right[right_index])
            right_index += 1

    for index, numbers in ((left_index, left), (right_index, right)):
        while index < len(numbers):
            merged_list.append(numbers[index])
            index += 1

    return merged_list

