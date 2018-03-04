"""
A minimum blockchain
	- understand how blocks are chain together
"""

import time
import json
import hashlib


class Block(object):
	
	"""
		a block	contain following information
			- index
			- timestamp
			- data : this will be transaction in case of currency
			- previous_hash : hash string of previous block
	"""

	def __init__(self, index, timestamp, data, previous_hash):
		self.index = index
		self.timestamp = timestamp
		self.data = data
		self.previous_hash = previous_hash



class BlockChain():

	"""
		a block chain manage following information
			- a chain of block
			- it's current transaction
	"""

	def __init__(self):
		# init a chain
		self.chain = []

		# define genesis_block
		genesis_block = Block(0, time.time(), 'this is first block', '0')

		# add genesis block to chain
		self.add_block_to_chain(genesis_block)


	def hash_block(self, block):
		
		# using json to convert from object to json string
		block_string = json.dumps(block.__dict__)

		# using hashlib to calculate sha256 of input json string
		return hashlib.sha256(json.dumps(block_string)).hexdigest()

	
	def add_block_to_chain(self, block):
		self.chain.append(block)


	def get_last_block(self):
		return self.chain[-1]


new_chain = BlockChain()

block_num = 5

# previous_hash = new_chain.hash_block(new_chain.get_last_block())
# print previous_hash

for index in range(1, block_num+1):
	previous_hash = new_chain.hash_block(new_chain.get_last_block())
	# print previous_hash
	time.sleep(0.2)
	new_block = Block(index, time.time(), 'this is block {0}'.format(index), previous_hash)
	new_chain.add_block_to_chain(new_block)


for block in new_chain.chain:
	print 'block'
	print json.dumps(block.__dict__, indent=4, sort_keys=False)
	print 'hash'
	print new_chain.hash_block(block)
	print '\n\n'