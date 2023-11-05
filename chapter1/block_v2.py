import hashlib
import json 

class Block:
    id = None
    history = None 
    parent_id = None
    parent_hash = None

block_A = Block()
block_A.id = 1 
block_A.history = 'Nelson likes cat'

block_B = Block()
block_B.id = 2
block_B.history = 'Marie likes dog'
block_B.parent_id = block_A.id 
block_B.parent_hash = hashlib.sha256(json.dumps(block_A.__dict__).encode('utf-8')).hexdigest()

block_C = Block()
block_C.id = 3
block_C.history = 'Sky hates dog'
block_C.parent_id = block_B.id
block_C.parent_hash = hashlib.sha256(json.dumps(block_B.__dict__).encode('utf-8')).hexdigest()


block_D = Block()
block_D.id = 4
block_D.history = 'Sky hates dog'
block_D.parent_id = block_C.id
block_serialized = json.dumps(block_D.__dict__).encode('utf-8')
print(block_serialized)



# The miner needs to guess the correct answer. If this puzzle is converted to
# Python code, it would be something like this:
answer = None
input = b'{"history": "Sky loves turtle", "parent_id": 3, "id": 4}' + answer
output = hashlib.sha256(input).hexdigest()
# //output  needs to be 
# 00000?????

# So, how could the miner solve a problem like this? We can use brute force:
payload = b'{"history": "Sky loves turtle", "parent_id": 3, "id": 4}'
for i in range(10000000):
    nonce = str(i).encode('utf-8')
    result = hashlib.sha256(payload+nonce).hexdigest()
    if result[0:5]=='00000':
        print(i)
        print(result)
        break