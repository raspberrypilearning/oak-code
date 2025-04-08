def populate_cipher(encrypt_key):
    caesar = {" " : " "} 
    for x in range(65, 91):
        key = chr(x)
        if x + encrypt_key > 90:
            pair = chr(x + encrypt_key - 26) 
        else:
            pair = chr(x + encrypt_key)
        caesar[key] = pair
    return caesar

print("What is the encryption key?")
encrypt_key = int(input())
caesar = (populate_cipher(encrypt_key))

print("Enter your text to encrypt")

plaintext = input().upper()
ciphertext = ""

for letter in plaintext:
    encrypted = caesar[letter]
    ciphertext = ciphertext + encrypted

print(ciphertext)
