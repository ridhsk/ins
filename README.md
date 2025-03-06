Playfair Cipher Encryption
This Python script implements the Playfair Cipher encryption technique, a classical encryption method that encrypts text using a 5x5 matrix generated from a keyword.

🔹 How It Works
Create a Playfair Matrix
A 5x5 matrix is generated using a given key.
The alphabet (A-Z) is used, but J is replaced with I.
Repeated letters in the key are removed.
Encrypt the Plaintext
The text is converted to uppercase, with J replaced by I.
If the plaintext length is odd, an "X" is added as padding.
The text is split into letter pairs and encrypted using Playfair Cipher rules:
Same row: Replace each letter with the next one in the row.
Same column: Replace each letter with the next one in the column.
Rectangle rule: Swap letters diagonally.

🔹 How to Run
Install Python (if not already installed).
Save the script as playfair.py.

Run the script:
python playfair_cipher.py
