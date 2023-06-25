def len(obj) -> int:
    c = 0
    while obj:
        c += 1
        obj = obj[1:]
    return c

def len(obj) -> int:
    c = 0
    for _ in obj:
        c += 1
    return c
