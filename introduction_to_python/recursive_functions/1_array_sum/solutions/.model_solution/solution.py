from typing import List, Union


def sum_array(numbers: List[Union[float, int]]) -> int:
    return 0 if numbers == [] else numbers.pop() + sum_array(numbers)

