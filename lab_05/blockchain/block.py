import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, itmestamp, transactions, proof):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = itmestamp
        self.transactions = transactions
        self.proof = proof
        self.hash = self.calculate_hash()
        
    def calculate_hash(self):
        data = str(self.index) + str(self.previous_hash) + str(self.timestamp) + str(self.transactions) + str(self.proof)
        return hashlib.sha256(data.encode()).hexdigest()