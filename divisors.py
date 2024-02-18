def divisors(n: int):
    ds = []
    for i in range(1, n+1):
        if not n % i:
            ds.append(i)
    return ds

def divisors(n: int):
    ds = []
    i = 1
    while i * i < n:
        if n % i == 0:
            ds.append(n)
            if i != n // i:
                ds.append(n//i)
        i += 1
    return ds
