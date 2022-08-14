# Imports 
import json 
import random 

from datetime import datetime 
from hashlib import sha256 

# Blockchain class 
class Blockchain(object): 
    def __init__(self): 
        self.chain = [] 
        self.pending_transactions = [] 

        # Creating the Genesis block 
        print("Creating the Genesis block") 
        self.chain.append(self.new_block())
    
    def new_block(self): 
        # Generating a new block and adding it to the chain 
        block = {
            'index': len(self.chain), 
            'timestamp': datetime.utcnow().isoformat(), 
            'transactions': self.pending_transactions, 
            'previous_hash': self.last_block["hash"] if self.last_block else None, 
            'nounce': format(random.getrandbits(64), "x"),
        }

        # Getting the hash of this new block and adding it to the block 
        block_hash = self.hash(block) 
        block["hash"] = block_hash 

        # Reseting the list of pending transactions 
        self.pending_transactions = [] 

        # Adding the block to the chain 
        # self.chain.append(block) 

        # print(f"Created block: {block['index']}") 
        return block 

    @staticmethod 
    def hash(block): 
        # First we need to ensure that the dictionary is sorted, otherwise we will have inconsistent hashes 
        block_string = json.dumps(block, sort_keys=True).encode() 
        return sha256(block_string).hexdigest() 

    @property
    def last_block(self): 
        # Getting the latest block in the chain 
        return self.chain[-1] if self.chain else None 
    
    @staticmethod 
    def valid_block(block): 
        # Checking of the block's hash starts with four zeros 
        return block["hash"].startswith("0000")

    def proof_of_work(self): 
        while True: 
            new_block = self.new_block() 
            if self.valid_block(new_block): 
                break
        
        self.chain.append(new_block) 
        print("Found a new block: ", new_block) 

    # def valid_hash(self):
    #     pass


    # def new_transaction(self, sender, recipient, amount): 
    #     # Adding a new transaction to the list of pending transactions. 
    #     self.pending_transactions.append({
    #         "recipient": recipient, 
    #         "sender": sender, 
    #         "amount": amount, 
    #     })

