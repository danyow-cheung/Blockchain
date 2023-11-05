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

print('block_B.__dict__\n',block_B.__dict__)


print('block_C.__dict__\n',block_C.__dict__)
'''
These blocks are different. By looking at these, we can be very sure that the
history has been altered. Consequently, Nelson would be caught redhanded. Now if Nelson wants to alter the history without getting caught, it
is not enough to change the history in block_A anymore. Nelson needs to
change all the parent_hash properties in every block (except block_A of course).
This is tougher cheating. With three blocks only, Nelson needs to change
two parent_hash properties. With a 1,000 blocks, Nelson needs to change 999
parent_hash properties!
'''