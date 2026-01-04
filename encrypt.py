import os
import re
import hashlib
import base64
from cryptography.fernet import Fernet

KEY_DIR = "keys"
ENC_DIR = "enc_files"
ITERATIONS = 100_000


def ensure_dirs():
    for d in [KEY_DIR, ENC_DIR]:
        os.makedirs(d, exist_ok=True)


def strong_password(password):
    if len(password) < 7:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    return True


def derive_key(password, salt):
    key = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        ITERATIONS,
        dklen=32
    )
    return base64.urlsafe_b64encode(key)


def main():
    ensure_dirs()

    # Password policy shown BEFORE input
    print("\n[!] Password Policy:")
    print("    - Minimum 7 characters")
    print("    - At least one uppercase letter")
    print("    - At least one lowercase letter")
    print("    - At least one number")

    print("[!] IMPORTANT: Remember your password. Losing it means permanent data loss.")
    password = input("Enter encryption password: ")

    if not strong_password(password):
        print("[-] Weak password detected. Encryption aborted.")
        return

    # Salt handling
    salt_path = os.path.join(KEY_DIR, "salt.bin")
    if not os.path.exists(salt_path):
        salt = os.urandom(16)
        with open(salt_path, "wb") as f:
            f.write(salt)
    else:
        with open(salt_path, "rb") as f:
            salt = f.read()

    key = derive_key(password, salt)
    with open(os.path.join(KEY_DIR, "secret.key"), "wb") as f:
        f.write(key)

    fernet = Fernet(key)

    # File path handling
    file_path = input("Enter file path to encrypt: ").strip().strip('"')

    if not os.path.exists(file_path):
        print("[-] File not found. Check path and try again.")
        return

    with open(file_path, "rb") as f:
        data = f.read()

    encrypted = fernet.encrypt(data)

    filename = os.path.basename(file_path)
    out_path = os.path.join(ENC_DIR, f"encrypted_{filename}")

    counter = 1
    while os.path.exists(out_path):
        out_path = os.path.join(ENC_DIR, f"encrypted_{counter}_{filename}")
        counter += 1

    with open(out_path, "wb") as f:
        f.write(encrypted)

    print(f"[+] Encryption successful: {out_path}")
    


if __name__ == "__main__":
    main()
