def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
