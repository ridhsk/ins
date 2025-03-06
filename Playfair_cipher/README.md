# **PLAYFAIR CIPHER IMPLEMENTATION**

## **ABOUT**
**This repository contains a Python implementation of the Playfair Cipher encryption and decryption technique.**

## **HOW IT WORKS**
**- Generates a 5x5 matrix using a keyword (excluding 'J').**  
**- Prepares the plaintext by replacing 'J' with 'I' and inserting 'X' if needed.**  
**- Encrypts or decrypts text based on Playfair cipher rules.**

## **USAGE**
**1. Run the script.**  
**2. Enter the plaintext message.**  
**3. Enter the keyword for encryption.**  
**4. The script outputs the encrypted and decrypted text.**

## **CODE**
**- `create_matrix(keyword)`: Generates the Playfair cipher matrix.**  
**- `find_position(matrix, char)`: Finds the position of a letter in the matrix.**  
**- `preprocess_text(plaintext)`: Prepares plaintext for encryption.**  
**- `playfair(plaintext, keyword, mode)`: Encrypts or decrypts the message.**

## **RUN THE CODE**
```sh
python playfair.py
```

## **EXAMPLE**
**Input:**  
**Enter the message to encrypt: HELLO**  
**Enter the keyword: SECRET**  

**Output:**  
**Encrypted Message: ??**  
**Decrypted Message: HELLO**
