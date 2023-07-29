def sqrt(n):
    return n ** 0.5

def sqrt(n):
    return n ** (1/2)

def sqrt(n :int):
    i = 0
    while i*i < n:
        i += 1
    a, b = i, i + 1
    for _ in range(99):
        r = (a + b)//2
        if r*r < n:
            a = r
        else:
            b = r
    return r

def sqrt(n):
    i = 0
    while not i*i < n < (i+1)*(i+1):
        i += 1
    a, b = i, i + 1
    for _ in range(99):
        r = (a + b)/2
        if r*r < n:
            a = r
        else:
            b = r
    return r
