# blockchain.py
import hashlib
import json
from datetime import datetime

class Block:
    def __init__(self, prev_hash, transactions):
        self.prev_hash = prev_hash
        self.transactions = transactions
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({"prev_hash": self.prev_hash, "transactions": self.transactions, "timestamp": self.timestamp})
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block("0", [])

    def add_block(self, block):
        block.prev_hash = self.chain[-1].hash
        block.hash = block.calculate_hash()
        self.chain.append(block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            prev_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.prev_hash != prev_block.hash:
                return False

        return True

# Usage
blockchain = Blockchain()
block = Block(blockchain.chain[-1].hash, ["Transaction 1", "Transaction 2"])
blockchain.add_block(block)
print("Is chain valid?", blockchain.is_chain_valid())
