def digital_sum(n: int):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def digital_sum(n: int):
    return sum([int(d) for d in str(n)])

def digital_sum(n: int):
    s = 0
    for d in str(n):
        s += int(d)
    return s
