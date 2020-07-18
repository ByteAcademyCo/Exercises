def factorial_recursive(integer: int) -> int:
    return 1 if integer is 0 else integer * factorial_recursive(integer - 1)

