def pow(x, y: int):
    p = 1
    while y:
        p *= x
        y -= 1
    return p

def pow(x, y):
    return x ** y
