def encrypt_xor_cipher(text, key):
    cipher = ""
    for char in text:
        cipher += chr(ord(char) ^ key)
    return cipher
