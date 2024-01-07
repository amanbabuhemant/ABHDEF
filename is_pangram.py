def is_pangram(text):
    letters = "abcdefghijklmnopqrstuvwxyz"
    for char in text:
        if not char.lower() in letters:
            return False
    return True

def is_pangram(text):
    letters = "abcdefghijklmnopqrstuvwxyz"
    return set(text.lower()) == set(letters)
