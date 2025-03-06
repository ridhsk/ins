# **FEISTEL CIPHER IMPLEMENTATION**

## **ABOUT**
**This script implements a basic Feistel cipher for encryption and decryption using bitwise operations.**

## **HOW IT WORKS**
**- Converts input text into an 8-bit binary format.**  
**- Splits the binary data into left and right halves.**  
**- Uses a user-provided key for encryption.**  
**- Performs Feistel rounds using bitwise XOR and addition operations.**  
**- Swaps left and right halves after each round.**  
**- Converts the final binary result back into text.**

## **USAGE**
**1. Run the script.**  
**2. Enter a string as input.**  
**3. Enter a key for encryption.**  
**4. The script outputs the encrypted binary and decrypts it back to plaintext.**

## **RUN THE CODE**
```sh
python feistel_cipher.py
```

## **EXAMPLE**
**Input:**  
**Enter a string: SECURITY**  
**Enter a key: 1234**  

**Output:**  
**Encrypted Binary: 101011000110...**  
**Decrypted Text: SECURITY**  
