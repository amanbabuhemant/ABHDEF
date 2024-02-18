def triangle_number(n):
    t = 0
    for i in range(1, n+1):
        t += i
    return t

def triangle_number(n):
    return sum(range(1, n+1))

def triangle_number(n):
    return (n*(n+1))//2

for n in range(10):
    print(triangle_number(n))
