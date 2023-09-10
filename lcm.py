def lcm(a: int, b: int) -> int:
    max = a if a > b else b
    while True:
        if not (max % a and max % b):
            return max
        max += 1

def lcm(a: int, b: int, max=None):
    if max is None:
        max = a if a > b else b
    if not (max % a and max % b):
        return max
    return lcm(a, b, max+1)

from gcd import gcd
def lcm(a: int, b: int) -> int:
    return (a * b) // gcd(a, b)
