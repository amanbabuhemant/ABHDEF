def ncr(n, r):
    numerator = 1
    denominator = 1
    for i in range(r):
        numerator *= n - i
        denominator *= i + 1
    return numerator // denominator

def ncr(n, r):
    if n < r:
        return 0
    else:
        return factorial(n) // (factorial(r) * factorial(n - r))
