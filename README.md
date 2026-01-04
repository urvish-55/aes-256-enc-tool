# Advanced Encryption Tool (AES-256)

## Overview

This project is a Python-based Advanced Encryption Tool developed as part of an internship task in Cyber Security and Ethical Hacking. The tool provides secure file encryption and decryption using modern cryptographic standards while remaining simple and understandable for educational use.

The application uses AES-256 symmetric encryption along with PBKDF2 (Password-Based Key Derivation Function 2) to derive strong encryption keys from user-provided passwords. Basic password strength validation is implemented to discourage insecure practices.

This project is intended strictly for educational and authorized use only.

---

## Key Features

- AES-256 encryption for secure file protection
- Password-based key derivation using PBKDF2
- Cryptographic salt generation and storage
- Separate handling of encrypted and decrypted files
- Password strength validation with user warnings
- Menu-driven interface for ease of use
- Clear separation of encryption and decryption logic

---

## Technologies Used

- Python 3.x
- cryptography library
- AES (Advanced Encryption Standard – 256 bit)
- PBKDF2 with SHA-256

---

## Project Structure

aes-256-enc-tool/
├─ aes_encryption_tool.py   # Main launcher (menu)
├─ encrypt.py               # Encryption logic
├─ decrypt.py               # Decryption logic
├─ keys/
│   ├─ salt.bin             # Cryptographic salt
│   └─ secret.key           # Derived encryption key (for demonstration)
├─ enc_files/               # Encrypted output files
└─ dec_files/               # Decrypted output files

---

## Installation

Ensure Python 3.x is installed.

Install the required dependency:

pip install cryptography

---

## How to Run

Navigate to the project directory and run:

python aes_encryption_tool.py

---

## How It Works

### Encryption

1. User selects the Encrypt File option.
2. A password strength warning is displayed.
3. User enters an encryption password.
4. Password strength is validated.
5. A cryptographic salt is generated or reused.
6. PBKDF2 derives a 256-bit AES key from the password.
7. The file is encrypted and saved in the enc_files directory.
8. The derived key and salt are stored in the keys directory.

### Decryption

1. User selects the Decrypt File option.
2. User enters the original encryption password.
3. The stored salt is reused to derive the same key.
4. The encrypted file is decrypted.
5. Output is saved in the dec_files directory.

---

## Password Security Notice

Weak passwords significantly reduce encryption strength and can be easily compromised.

Users are advised to use passwords that include:
- At least 7 characters
- Uppercase letters
- Lowercase letters
- Numbers

The tool warns users if a weak password is detected before encryption proceeds.

---

## Scope and Limitations

This project focuses on:
- Secure file encryption
- Proper key derivation
- Safe storage of cryptographic materials

It does not include:
- Public-key cryptography
- Digital signatures
- Network-based encryption
- Key exchange protocols

These exclusions are intentional to keep the project aligned with internship scope.

---

## Ethical Usage Disclaimer

This project is intended strictly for educational purposes and authorized environments.

Unauthorized use against systems, files, or data without explicit permission is strictly prohibited.

---

## License

This project is licensed under the MIT License.
See the LICENSE file for details.

---

## Author

Urvish Kharate
