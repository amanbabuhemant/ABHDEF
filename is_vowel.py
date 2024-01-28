def is_vowel(char):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    return char in vowels

def is_vowel(char):
    vowels = ["a", "e", "i", "o", "u"]
    return char.lower() in vowels

def is_vowel(char):
    return char.lower() in set("aeiou")
