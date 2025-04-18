# OneTimePad
An unbreakable text substitution cipher. It meets and exceeds AES-256 encryption strength due to it being information-theoretic security based. This is backed by rigorous mathematical and cryptographical analysis. Easy to use.

---

# Uncrackable Substitution Cipher

ClatsOTP

Version 1.00 CLI (GUI coming soon) 

By Joshua M Clatney – Ethical Pentesting Enthusiast

## Overview

This Python script implements a simple, unbreakable substitution cipher for encrypting and decrypting text. It features a command-line interface with an ASCII art header and uses a fixed key generated from a Lorem Ipsum text. The cipher works by shifting each letter in the input text by a corresponding letter in the key. Please note, in order for this cipher to be perfectly secure, you should NOT reuse the text used as the key. This script uses the same text, Lorem Ipsum repeated 5 times, which means you can encrypt up to 2500 characters unless you lengthen it. You can do this by opening the script and pasting in your own random text in the appropriate section. With a block of text that's 500 words long, with an average of 5 letters per word (2500 letters), the keyspace will be 2^11,751 which is massive compared to the AES keyspace of 2^256. AES-256 has a keyspace that's number is larger than the amount of atoms in the observable universe, meaning the One Time Key's keyspace is 45x more than AES-256. A sophisticated adversary with unlimited computational power would not be able to break the cipher even if it’s attempting to brute force at 100 septillion keys per millisecond for an infinite period. By that time, everyone would be dead anyways due to heat death and entropy (the sun is constantly expanding and will eventually burn everyone to death and cook the earth), so forget about trying to break the cipher. It will not happen if it's implemented correctly. 

## Features

- **ASCII Art Header:**  
  Displays a colorful banner along with the title, version, and author information using ANSI escape codes.

- **Key Generation:**  
  - **Raw Key:** A Lorem Ipsum text is repeated 5 times.  
  - **Processed Key:** The raw key is converted to uppercase and filtered to include only letters A–Z.
  
- **Encryption:**  
  Each uppercase letter of the plaintext is shifted by the alphabetical value of a corresponding letter from the key (using modular arithmetic). Non-alphabet characters are preserved.
  
- **Decryption:**  
  Reverses the encryption process by subtracting the key's shift values from the ciphertext letters.

- **User Interaction:**  
  The user is prompted to select an option (encrypt or decrypt) and then input the relevant text. The script checks if the input text’s letter count exceeds the processed key’s length and aborts if it does.

## How It Works

1. **Display Header:**  
   The `print_header()` function prints the ASCII art header with colored text.

2. **Key Generation and Processing:**  
   - `generate_key()` creates a long string by repeating a Lorem Ipsum passage.
   - `process_key()` converts this string to uppercase and removes any characters that are not A–Z, ensuring only valid letters are used for shifting.

3. **Encryption Algorithm:**  
   - The `encrypt()` function iterates through the plaintext.  
   - For each uppercase letter, it calculates the shift based on the corresponding letter from the key.
   - The new letter is computed using a modulo 26 operation to wrap around the alphabet.

4. **Decryption Algorithm:**  
   - The `decrypt()` function similarly processes each letter in the ciphertext.  
   - It subtracts the key’s letter value to retrieve the original letter, again using modular arithmetic.

5. **Program Flow:**  
   - The `main()` function ties everything together: displaying the header, generating the key, prompting the user for input, performing validation (i.e., ensuring the key is long enough for the text), and finally executing encryption or decryption based on the user's choice.

## Usage Instructions

1. **Run the Script:**  
   Execute the script in a terminal or by downloading it using Python 3x.

2. **Select an Option:**  
   - Enter `1` for encryption.
   - Enter `2` for decryption.

3. **Input Your Text:**  
   Type your plaintext (for encryption) or ciphertext (for decryption).

4. **View the Result:**  
   The script outputs the encrypted ciphertext or decrypted plaintext. If the text contains more letters than the key length, an error is displayed.

5. **Exit:**  
   The script waits for you to press Enter before closing.

## Limitations and Considerations

- **Static Key:**  
The key is derived from a repeated Lorem Ipsum text, making it predictable and unsuitable for serious security purposes **ONLY IF THE SAME KEY IS USED AGAIN**. If you need this to be perfectly secure and ensure it is uncrackable, you can only use the Lorem Ipsum once, then you must change it. However, it will still be highly secure and unbreakable unless you encrypt a second block of text with the same key to the same person.

- **Key Length Constraint:**  
  The script enforces that the number of alphabetic characters in the input does not exceed the length of the processed key. This means very long texts may trigger an error and requires a modification, by either lengthening the key string, or increasing how many times the key is multiplied by. 

- **Encryption Simplicity:**  
  This cipher is a simple substitution method, but is not vulnerable to standard cryptanalysis techniques like frequency analysis or Friedman analysis. The Caeser, ROT13, and Vigenere (including the Autokey varient) can all be decrypted by various means, the first 2 can be decrypted by simply pasting the ciphertext into ChatGPT, the Vigenere cannot be broken by ChatGPT due to the variable shift, but One Time Pad CANNOT be broken by anyone when used properly. 

- **Case Sensitivity:**  
  The script converts all input to uppercase. 

## License

Distributed under the Apache 2.0 License. 

**Author**

Joshua M Clatney (Clats97)

Ethical Pentesting Enthusiast

Copyright 2025 Joshua M Clatney (Clats97) 


