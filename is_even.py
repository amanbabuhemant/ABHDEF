#ckeck the number is even or not, return bool

def is_even(n: int) -> bool:
    return n % 2 == 0

def is_even(n: int) -> bool:
    return n & 1 == 0

def is_even(n: int) -> bool:
    return [True, False][n % 2]
