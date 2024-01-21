def is_isogram(s):
    s = s.lower()
    for c in s:
        if s.count(c) > 1:
            return False
    return True

def is_isogram(s):
    return len(s.lower()) == len(set(s.lower()))
