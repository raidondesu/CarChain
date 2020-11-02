import hashlib
import json
from urllib.parse import urlparse
from CSV import CSV
from DBConnect import DBConnect

class Blockchain:
    
    def __init__(self):

        self.csv_operator = CSV()
        
    def get_hash(self, block):
        
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def proof_of_work(self, previous_nonce):
        new_nonce = 1
        check_nonce = True
        while check_nonce:
            hash_operation = hashlib.sha256(str(new_nonce**2 - previous_nonce**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_nonce = False
            else:
                new_nonce += 1
        return new_nonce
    
    def chain_is_valid(self):

        for previous_block, current_block in self.csv_operator.read_chain():
            
            if self.get_hash(previous_block) != current_block["hash"]["block"]:
                
                return False
            
            hash_operation = hashlib.sha256(str(current_block["nonce"]**2 - previous_block["nonce"]**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':

                return False
           
        return True
    
    def add_genesis_block(self):
        
        block = {"_id":0, 
                 "car_id":"None",
                 "nonce":0,
                 "hash": {"block":"None","car":"None"}, 
                 "details": {"block_type":"None"}}    
        self.chain.append(block)
                        
    def mine_block(self, block_type, block_data):
        
        client = DBConnect()
        
        last_block = self.csv_operator.get_last_block()
        _id = self.csv_operator.get_chain_length()
        car_id = block_data[0]
        nonce = self.proof_of_work(last_block["nonce"])
        last_hash_block = self.get_hash(last_block)
        last_hash_car = "None"
        
        if block_type == "Production":
            
            block = {"_id":_id,
                     "car_id":car_id,
                     "nonce":nonce,
                     "hash": {"block":last_hash_block,
                              "car":last_hash_car},
                     "details": {"block_type":"Production"}     
            }
            
        elif block_type == "NewRegister":
            
            block = {"_id":_id,
                     "car_id":car_id,
                     "nonce":nonce,
                     "hash": {"block":last_hash_block,
                              "car":last_hash_car},
                     "details": {"block_type": "NewRegister"   
                                } 
                    }
                                 
        elif block_type == "Repair":
            
            last_car_entry = client.get_car_history(car_id)[-1]
            last_hash_car = self.get_hash(last_car_entry)            
            
            block = {"_id":_id,
                     "car_id":car_id,
                     "nonce":nonce,
                     "hash": {"block":last_hash_block,
                              "car":last_hash_car},
                     "details": {"block_type": "Repair",
                                } 
                    }
         
        elif block_type == "Sale":
            
            last_car_entry = client.get_car_history(car_id)[-1]
            last_hash_car = self.get_hash(last_car_entry)    
            
            block = {"_id":_id,
                     "car_id":car_id,
                     "nonce":nonce,
                     "hash": {"block":last_hash_block,
                              "car":last_hash_car},
                     "details": {"block_type": "Sale"}  
                    }
                                                                     
        else:
        
            return "wrong input"
        
        client.ingest_block(block)
        self.csv_operator.add_block(block)
        
          
    def car_history_is_valid(self,car_id):
        
        """
        car history is valid if
        1. chain is valid
        2. entries in data base match corresponding chain entries
        3. the hashes that link the car history are valid
        """
  
        if self.chain_is_valid():
        
            client = DBConnect()
            car_history = client.get_car_history(car_id)
            
            for stage in car_history:
                
                if stage != self.chain[stage["_id"]]:
                    
                    return False
            
            if len(car_history) <= 1:
                
                return True
            
            index = 1
            
            while index < len(car_history):
                
                if self.get_hash(car_history[index -1]) != car_history[index]["hash"]["car"]:
                    
                    return False
                
                index += 1
                
            return True
                
        else:
            
            return False
        
    def replace_chain(self): 
        
        longest_chain = None
        max_length = len(self.chain)
        
        for node in self.nodes:
            response = requests.get(f'http://{node}/get_chain')
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']
                if length > max_length and self.is_chain_valid(chain):
                    max_length = length
                    longest_chain = chain
        if longest_chain:
            self.chain = longest_chain
            return True
        return False
            


test = Blockchain()
test.mine_block("Sale", ["1111"])
        