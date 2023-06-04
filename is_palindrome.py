#Check the given string, number or list is palindrome or not.

def is_palindrome(n: int) -> bool:
    r = 0
    t = n
    while n > 0:
        r = r * 10 + n % 10
        n //= 10
    return r == t

def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def is_palindrome(s: list) -> bool:
    s = list(s)
    return s == s[::-1]

def is_palindrome(s) -> bool:
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def is_palindrome(s) -> bool:
    s = str(s)
    return s == s[::-1]
