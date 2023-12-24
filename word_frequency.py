def word_frequency(text: str) -> dict:
    words = text.split()
    word_f = {}
    for word in words:
        w = word.strip(".,!?").lower()
        word_f[w] = word_f.get(w,0)+1
    return word_f
