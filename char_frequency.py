def char_frequency(string):
    freq = {}
    for c in string:
        freq[c] = freq.get(c,0)+1
    return freq
