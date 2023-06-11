def sum(*nums):
    s = 0
    for i in nums:
        s += i
    return s

def sum(*nums: int):
    s = 0
    for n in nums:
        while n != 0:
            c = s & n
            s = s ^ n
            n = c << 1
    return s

def sum(iterable, start=0):
    for i in iterable:
        start += i
    return start
