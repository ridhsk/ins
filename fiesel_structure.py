from Crypto.Cipher import DES
import binascii


def pad(text):
    while len(text) % 8 != 0:
        text += " "
    return text


def des_encrypt(plain_text, key):
    cipher = DES.new(key, DES.MODE_ECB)  
    padded_text = pad(plain_text) 
    encrypted_text = cipher.encrypt(padded_text.encode())  
    return binascii.hexlify(encrypted_text).decode()  


def des_decrypt(encrypted_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_text = cipher.decrypt(binascii.unhexlify(encrypted_text))
    return decrypted_text.decode().strip()  


plain_text = input("Enter text to encrypt: ")
key = input("Enter 8-character key: ")


if len(key) != 8:
    print("Error: Key must be exactly 8 characters!")
else:
    encrypted_text = des_encrypt(plain_text, key.encode())
    decrypted_text = des_decrypt(encrypted_text, key.encode())

 
    print(f"Plain Text: {plain_text}")
    print(f"Encrypted Text (Hex): {encrypted_text}")
    print(f"Decrypted Text: {decrypted_text}")