from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
        return key

def load_key():
    return open("secret.key", "rb").read()

def encrypt_message(password):
    try:
        key = load_key()
    except:
        key = generate_key()
    f = Fernet(key)
    return f.encrypt(password.encode())

def decrypt_message(password):
    try:
        key = load_key()
    except:
        key = generate_key()
    f = Fernet(key)
    return f.decrypt(password).decode()