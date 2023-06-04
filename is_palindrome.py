#Check the given string, number or list is palindrome or not.

def is_palindrome(n: int):
    r = 0
    t = n
    while n > 0:
        r = r * 10 + n % 10
        n //= 10
    return r == t

def is_palindrome(s: str):
    return s == s[::-1]

def is_palindrome(s: list):
    s = list(s)
    return s == s[::-1]

def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def is_palindrome(s):
    s = str(s)
    return s == s[::-1]
