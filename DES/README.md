# **DES KEY GENERATION**

## **ABOUT**
**This repository contains a Python implementation of DES key generation using bitwise operations and randomization.**

## **HOW IT WORKS**
**- Converts input text to an 8-bit binary format.**  
**- Removes specific bits to reduce the binary size.**  
**- Splits binary into left and right halves.**  
**- Applies left shift operations using predefined shift values.**  
**- Generates 8 unique keys by introducing randomness.**

## **USAGE**
**1. Run the script.**  
**2. Enter any string as input.**  
**3. The script generates 8 unique keys for DES encryption.**

## **CODE**
**- Converts input text to binary.**  
**- Splits binary into left and right halves.**  
**- Uses left shift and random bit selection for key generation.**  

## **RUN THE CODE**
```sh
python des_keygen.py
```

## **EXAMPLE**
**Input:**  
**Enter any string: SECURITY**  

**Output:**  
**Key 1 = 110101000110...**  
**Key 2 = 101011001100...**  
**Key 3 = 010110101001...**  
**...**  
**Key 8 = 111000110010...**  
