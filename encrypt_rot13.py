def encrypt_rot13(text):
    cipher = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            cipher += chr((ord(char) - offset + 13) % 26 + offset)
        else:
            cipher += char
    return cipher
