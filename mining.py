# mining.py
import time
import hashlib  # Need to import hashlib for the hash function
from blockchain import Block  # Import the Block class from blockchain.py

class Miner:
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def mine_block(self, transactions):
        prev_hash = self.blockchain.chain[-1].hash if self.blockchain.chain else "0"  # Check if blockchain has blocks
        new_block = Block(prev_hash, transactions)
        
        # Proof of Work
        nonce = 0
        while not self.valid_proof(prev_hash, transactions, new_block.timestamp, nonce):
            nonce += 1

        new_block.hash = new_block.calculate_hash()
        self.blockchain.add_block(new_block)

    def valid_proof(self, prev_hash, transactions, timestamp, nonce):
        guess = f'{prev_hash}{transactions}{timestamp}{nonce}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:2] == "00"

# Usage
# You need to instantiate the Blockchain class and pass it 
