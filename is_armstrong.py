def is_armstrong(n: int):
    n = str(n)
    p = len(n)
    s = 0
    for d in n:
        s += int(d)**p
    return int(n) == s

def is_armstrong(n: int):
    p = 0
    t = n
    while t:
        p += 1
        t //= 10
    s = 0
    t = n
    while t:
        s += (t % 10)** p
        t //= 10
    return s == n
