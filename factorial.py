#Calculate the factorial of given number

def factorial(n: int) -> int:
    if n == 0:
        return 1
    return factorial(n-1) * n

def factorial(n: int) -> int:
    f = 1
    while n:
        f *= n
        n -= 1
    return f
