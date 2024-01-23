import sys
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
import base64
import getpass

def get_key(password: str) -> bytes:
    password = password.encode()
    salt = b'salt_'  # Should be unique per user, you can use os.urandom(16) to generate a salt
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key

def encrypt(filename: str, password: str):
    key = get_key(password)
    cipher_suite = Fernet(key)
    with open(filename, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher_suite.encrypt(file_data)
    with open(filename + '.LEX', 'wb') as file:
        file.write(bytes(filename, 'utf-8') + b'\0' + encrypted_data)

def decrypt(filename: str, password: str):
    key = get_key(password)
    cipher_suite = Fernet(key)
    with open(filename, 'rb') as file:
        file_data = file.read()
    original_filename, encrypted_data = file_data.split(b'\0', 1)
    try:
        decrypted_data = cipher_suite.decrypt(encrypted_data)
    except InvalidToken:
        print("Error: The password is incorrect.")
        return
    with open(original_filename.decode('utf-8'), 'wb') as file:
        file.write(decrypted_data)

def main():
    if len(sys.argv) != 3:
        print("Usage: python crypt.py [encrypt/decrypt] [filename]")
        sys.exit(1)
    password = getpass.getpass("Enter your password: ")
    operation = sys.argv[1]
    filename = sys.argv[2]
    if operation == 'encrypt':
        encrypt(filename, password)
    elif operation == 'decrypt':
        decrypt(filename, password)
    else:
        print("Invalid operation. Please choose either 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
