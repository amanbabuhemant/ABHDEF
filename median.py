def median(series):
    s = series.copy()
    s.sort()
    n = len(s)
    if n % 2 == 1:
        return s[n // 2]
    return (s[n//2]+s[(n//2)-1])/2

def median(*series):
    s = sorted(series)
    n = len(s)
    if n % 2 == 1:
        return s[n // 2]
    return (s[n//2]+s[(n//2)-1])/2
