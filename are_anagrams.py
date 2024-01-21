def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    for c in s1:
        if s1.count(c) != s2.count(c):
            return False
    return True

def are_anagrams(s1, s2):
    l1 = list(s1)
    l2 = list(s2)
    l1.sort()
    l2.sort()
    return l1 == l2

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)
