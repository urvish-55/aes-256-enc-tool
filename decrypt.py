import os
import hashlib
import base64
from cryptography.fernet import Fernet

KEY_DIR = "keys"
DEC_DIR = "dec_files"
ITERATIONS = 100_000


def ensure_dirs():
    for d in [KEY_DIR, DEC_DIR]:
        os.makedirs(d, exist_ok=True)


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

    password = input("Enter decryption password: ")

    salt_path = os.path.join(KEY_DIR, "salt.bin")
    if not os.path.exists(salt_path):
        print("Salt file missing.")
        return

    with open(salt_path, "rb") as f:
        salt = f.read()

    key = derive_key(password, salt)
    fernet = Fernet(key)

    file_path = input("Enter encrypted file path: ").strip()
    if not os.path.exists(file_path):
        print("Encrypted file not found.")
        return

    with open(file_path, "rb") as f:
        encrypted = f.read()

    try:
        decrypted = fernet.decrypt(encrypted)
    except Exception:
        print("[-] Decryption failed. Wrong password or corrupted file.")
        return

    filename = os.path.basename(file_path).replace("encrypted_", "")
    out_path = os.path.join(DEC_DIR, f"decrypted_{filename}")

    counter = 1
    while os.path.exists(out_path):
        out_path = os.path.join(DEC_DIR, f"decrypted_{counter}_{filename}")
        counter += 1

    with open(out_path, "wb") as f:
        f.write(decrypted)

    print(f"[+] Decryption successful: {out_path}")


if __name__ == "__main__":
    main()
