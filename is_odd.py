#check the number is odd or not, return bool

def is_odd(n: int) -> bool:
    return n % 2 == 1

def is_odd(n: int) -> bool:
    return n & 1 == 1

def is_odd(n: int) -> bool:
    return [False, True][n % 2]
