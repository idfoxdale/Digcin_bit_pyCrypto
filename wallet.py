# wallet.py
import hashlib
import secrets

class Wallet:
    def __init__(self):
        self.private_key = secrets.token_hex(32)
        self.public_key = self.generate_public_key()

    def generate_public_key(self):
        sha256 = hashlib.sha256()
        sha256.update(self.private_key.encode())
        return sha256.hexdigest()

# Usage
wallet = Wallet()
print("Private Key:", wallet.private_key)
print("Public Key:", wallet.public_key)
