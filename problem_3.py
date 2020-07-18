import sys

class PriorityQueue(object):
  
    def __init__(self):
        self.queue = []
    
    def extract_min(self):
        return self.queue.pop(0) # O(n) because of left-shifting
    
    def insert(self, node): # inserts a node and maintains increasing sorted order. O(n)
        size = len(self.queue)
        self.queue.append(node)
        for i in reversed(range(size)):
            if self.queue[i + 1] >= self.queue[i]:
                break
            self.queue[i], self.queue[i + 1] = self.queue[i + 1], self.queue[i]
    
    def peek(self): # O(1)
        if self.queue:
            return self.queue[0]



from collections import defaultdict

class huffmanNode(object):
  
    def __init__(self, char, freq, left = None, right = None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
  
    def __ge__(self, other): #need this bc Python doesn't know how to compare nodes
        return True if self.freq >= other.freq else False
  
    def __lt__(self, other):
        return True if self.freq < other.freq else False
    
    def __repr__(self):
        return str((self.char, self.freq))

    
def huffman_encoding(data):
    #############################
    # Calculate the frequencies #
    #############################
    #frequencies = defaultdict(int)
    #for char in string:
    #  frequencies[char] += 1
  
    frequencies = {}
    for char in data:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    
  #############################################
  # Create the priority queue (as a min-heap) #
  #############################################
  #nodes = [huffmanNode(char, freq) for char, freq in frequencies.items()]
  
    nodeList = []
    for key in frequencies:
        nodeList.append(huffmanNode(key, frequencies[key]))
  
    queue = PriorityQueue()
    for node in nodeList: # O(n^2)
        queue.insert(node) #because insert goes through the entire thing, it ends up being sorted
  
  ###################################################
  # Create the Huffman tree from the priority queue #
  ###################################################
  #  
    for i in range(len(nodeList) - 1): # this for-loop runs len(nodeList) - 1 times
        node1 = queue.extract_min()
        node2 = queue.extract_min()
        print(node1)
        print(node2)
        print()
        
        char = node1.char + node2.char
        freq = node1.freq + node2.freq
        
        node3 = huffmanNode(char, freq, node1, node2)  
        queue.insert(node3)
    
    root = queue.extract_min()

    #############################################################
    # Get the mapping of char-to-encoding from the Huffman tree #
    #############################################################
    mapping = expand(root)   #~ O(n)
    
    #########################################################################
    # Get the encoded bit-string from the original string using the mapping #
    #########################################################################

    print(mapping)
    encoding = ''
    # "" -> "10" -> "1010" -> ...
    for char in data: #O(n)
        encoding += mapping[char] #O(1)
   
    #################################################################
    # Return both the bit-string encoding and the Huffman Tree root #
    #################################################################
    return encoding, root
    

def expand(node, mapping={}, code=""): # Expand on root
    if node.left is not None:
        expand(node.left, mapping, code + "0")
        expand(node.right, mapping, code + "1")
  
    elif code == "": # in case of a string with only one (possibly repeated) character.
        mapping[node.char] = '1' # AAAAAAAAAA -> 1111111111111
    
    else:
        mapping[node.char] = code
    
    return mapping


def huffman_decoding(encoded_string,root):
    node = root
    decoded_message = ""

    for bit in encoded_string:
        if bit == "1" and node.right is not None:
            node = node.right
        
        elif bit == "0" and node.left is not None:
            node = node.left
        
        if node.left is None:
            decoded_message += node.char
            node = root
     
    return decoded_message
        

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "AAAAAAABBBCCCCCCCDDEEEEEE"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))