# **HILL CIPHER ENCRYPTION**

## **ABOUT**
**This script implements the Hill Cipher encryption technique using matrix multiplication and modular arithmetic.**

## **HOW IT WORKS**
**- Converts the input text into numerical values (A=0, B=1, ..., Z=25).**  
**- Uses a predefined key matrix for encryption.**  
**- Pads the plaintext if necessary to match the matrix size.**  
**- Encrypts the plaintext using matrix multiplication and modulo 26 operations.**  
**- Converts the encrypted numerical values back to letters to form the ciphertext.**

## **USAGE**
**1. Run the script.**  
**2. Enter a plaintext message.**  
**3. The script encrypts the message using the Hill Cipher method.**  
**4. Outputs the ciphertext.**

## **RUN THE CODE**
```sh
python hill_cipher.py
```

## **EXAMPLE**
**Input:**  
**Enter the plaintext: HELLO**  

**Output:**  
**Encrypted: XZBXX**  
