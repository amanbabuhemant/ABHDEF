def encrypt_caesar_cipher(text, shift):
    cipher = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            cipher += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            cipher += char
    return cipher
