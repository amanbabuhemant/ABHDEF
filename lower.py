def lower(s: str) -> str:
    u = "QWERTYUIOPASDFGHJKLZXCVBNM"
    l = "qwertyuiopasdfghjklzxcvbnm"
    for c in s:
        if c in u:
            s = s.replace(c, l[u.find(c)])
    return s

def lower(s: str) -> str:
    ul = {"Q":"q","W":"w","E":"e",
    "R":"r","T":"t","Y":"y","U":"u",
    "I":"i","O":"o","P":"p","A":"a",
    "S":"s","D":"d","F":"f","G":"g",
    "H":"h","J":"j","K":"k","L":"l",
    "Z":"z","X":"x","C":"c","V":"v",
    "B":"b","N":"n","M":"m"}
    for c in s:
        s = s.replace(c,ul.get(c,c))
    return s

def lower(s: str) -> str:
    for c in s:
        o = ord(c)
        if 64 < o < 90:
            s = s.replace(c, chr(o+32))
    return s
