import random
import string

# Create character list
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

# Create shuffled key
key = chars.copy()
random.shuffle(key)

print(f'Key: {"".join(key)}')

# ENCRYPT
plainText = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plainText:
    if letter in chars:
        index = chars.index(letter)
        cipher_text += key[index]
    else:
        cipher_text += letter

print(f"\nEncrypted message: {cipher_text}")

# DECRYPT
decrypt_text = ""

for letter in cipher_text:
    if letter in key:
        index = key.index(letter)
        decrypt_text += chars[index]
    else:
        decrypt_text += letter

print(f"Decrypted message: {decrypt_text}")