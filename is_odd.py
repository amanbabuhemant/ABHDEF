def is_odd(n: int) -> bool:
    if n == 1:
        return True
    if n == 0:
        return False
    return is_odd(n-2)

def is_odd(n: int) -> bool:
    return n % 2 == 1

def is_odd(n: int) -> bool:
    return n & 1 == 1

def is_odd(n: int) -> bool:
    return [False, True][n % 2]
