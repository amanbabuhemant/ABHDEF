def npr(n, r):
    return factorial(n) // factorial(n-r)

def npr(n, r):
    result = 1
    for i in range(r):
        result *= n - i
    return result
