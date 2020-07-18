def merge_sort(numbers: list) -> list:
    numbers_length = len(numbers)

    if numbers_length < 2:
        return numbers

    middle_index = numbers_length // 2
    left_half = numbers[:middle_index]
    right_half = numbers[middle_index:]

    return _merge(merge_sort(left_half), merge_sort(right_half))


def _merge(left: list, right: list) -> list:
    total_length = len(left) + len(right)
    merged_list = [None] * total_length

    left_index = right_index = merged_list_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged_list[merged_list_index] = left[left_index]
            left_index += 1
        else:
            merged_list[merged_list_index] = right[right_index]
            right_index += 1

        merged_list_index += 1

    for list_index, list_ in ((left_index, left), (right_index, right)):
        while list_index < len(list_):
            merged_list[merged_list_index] = list_[list_index]
            list_index += 1
            merged_list_index += 1

    return merged_list
