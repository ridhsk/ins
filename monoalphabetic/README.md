# **MONOALPHABETIC CIPHER ENCRYPTION & DECRYPTION IN C**

## **ABOUT**
**This program implements the Monoalphabetic Cipher, a substitution cipher where each letter in the plaintext is replaced with a fixed different letter.**  

## **HOW IT WORKS**
**- A fixed mapping of letters is used for encryption.**  
**- The decryption process reverses the mapping to retrieve the original text.**  
**- Unlike Caesar Cipher, the shift is not uniform, making it more secure.**  

## **USAGE**
**1. Compile and run the C program.**  
**2. Enter the plaintext message.**  
**3. Provide the custom key or mapping.**  
**4. The program will output the encrypted and decrypted text.**

## **COMPILATION & EXECUTION**
```sh
gcc monoalphabetic_cipher.c -o monoalphabetic_cipher
./monoalphabetic_cipher
```

## **EXAMPLE**
**Input:**  
**Plaintext: HELLO**  
**Key Mapping: A → D, B → E, C → F, ..., Z → C**  

**Output:**  
**Encrypted text: KHOOR**  
**Decrypted text: HELLO**  
