import hashlib



class Block(object):

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
    
    def calc_hash(self):
      hash_str = self.timestamp + self.previous_hash + "".join(self.data)
      hash_str = hash_str.encode('utf-8')  
    
      sha = hashlib.sha256()
      sha.update(hash_str)

      return sha.hexdigest()
      
class Node(object):
  
    def __init__(self, prev=None, nxt=None, Block):
      self.prev = prev
      self.next = nxt
      self.block = Block
      
class DLL(object):
    
    def __init__(self):
      self.head = None
      self.tail = None
    
    def add_block(data):
      current = self.head
      while current.next is not None:
        current = current.next #to get to the end
      previous_hash = current.block.hash
      times.gmtime() #might be an integer, might have to cast to str
      
      new_block_node = Node(Block(times, data, previous_hash), current) #
      current.next = new_block_node