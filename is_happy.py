def is_happy(n: int):
    n = str(n)
    while len(n) != 1:
        s = 0
        for d in n:
            s += int(d)*int(d)
        n = str(s)
    return n in "17"

def is_happy(n: int):
    n = str(n)
    while len(n) != 1:
        s = 0
        for d in n:
            s += int(d)**2
        n = str(s)
    return n in {"1", "7"}

def is_happy(n: int):
    while n > 9:
        s = 0
        t = n
        while t:
            s += (t%10) **2
            t //= 10
        n = s
    return n == 1 or n == 7

def is_happy(n: int):
    while n > 9:
        n = sum(int(d)**2 for d in str(n))
    return n == 1 or n == 7
