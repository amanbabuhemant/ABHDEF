def is_even(n: int) -> bool:
    if n == 1:
        return False
    if n == 0:
        return True
    return is_even(n-2)

def is_even(n: int) -> bool:
    return n % 2 == 0

def is_even(n: int) -> bool:
    return n & 1 == 0

def is_even(n: int) -> bool:
    return [True, False][n % 2]
