def is_consonant(char):
    consonants = [
        "b", "c", "d", "f", "g", "h",
        "j", "k", "l", "m", "n", "p",
        "q", "r", "s", "t", "v", "w",
        "x", "y", "z", "B", "C", "D",
        "F", "G", "H", "J", "K", "L",
        "M", "N", "P", "Q", "R", "S",
        "T", "V", "W", "X", "Y", "Z",
    ]
    return char in consonants

def is_consonant(char):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    return not char in vowels

def is_consonant(char):
    vowels = ["a", "e", "i", "o", "u"]
    return not char.lower() in vowels

def is_consonant(char):
    return not char.lower() in set("aeiou")

def is_consonant(char):
    consonants = "bcdfghjklmnpqrstvwxyz"
    return char.lower() in consonants
