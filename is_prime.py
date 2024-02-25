def is_prime(n):
    if n < 2:
        return False
    devisors = 0
    for i in range(1, n+1):
        if n % i == 0:
            devisors += 1
    return devisors < 3

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if not n % i:
            return False
    return True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n//2+1):
        if not n % i:
            return False
    return True

