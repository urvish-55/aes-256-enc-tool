#!/usr/bin/env python3
"""
Advanced Encryption Tool (AES-256)
Author: <Urvish Kharate>
Internship Task 4 - CODTECH

Description:
This is the main launcher for the Advanced Encryption Tool.
It allows the user to choose between:
- File Encryption
- File Decryption

The actual cryptographic operations are handled
by separate modules (encrypt.py and decrypt.py).

Encryption Details:
- AES-256 is used for encrypting files
- PBKDF2-HMAC-SHA256 is used to derive a secure key from a user password
- Keys and salts are stored securely for future use
"""


import os

def main():
    while True:
        print("\n=== Advanced Encryption Tool (AES-256) ===")
        print("1. Encrypt File")
        print("2. Decrypt File")
        print("3. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            os.system("python encrypt.py")
        elif choice == "2":
            os.system("python decrypt.py")
        elif choice == "3":
            print("Exiting.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
