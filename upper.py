def upper(s: str) -> str:
    u = "QWERTYUIOPASDFGHJKLZXCVBNM"
    l = "qwertyuiopasdfghjklzxcvbnm"
    for c in s:
        if c in l:
            s = s.replace(c, u[l.find(c)])
    return s

def upper(s: str) -> str:
    lu = {"q":"Q","w":"W","e":"E",
    "r":"R","t":"T","y":"Y","u":"U",
    "i":"I","o":"O","p":"P","a":"A",
    "s":"S","d":"D","f":"F","g":"G",
    "h":"H","j":"J","k":"K","l":"L",
    "z":"Z","x":"X","c":"C","v":"V",
    "b":"B","n":"N","m":"M"}
    for c in s:
        s = s.replace(c,lu.get(c,c))
    return s

def upper(s: str) -> str:
    for c in s:
        o = ord(c)
        if 94 < o < 123:
            s = s.replace(c, chr(o-32))
    return s
