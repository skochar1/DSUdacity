class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def has(self, value):
        current = self.head
        while current:
            if value == current.value:
                return True
            current = current.next
        return False

def intersection(llist_1, llist_2):
    result = LinkedList()
    
    node = llist_1.head
    # can access both node.value and node.next
    
    while node:
        v = node.value
        if llist_2.has(v) and not result.has(v):
            result.append(v)
        node = node.next
      
    return result

def union(llist_1, llist_2):
    result = LinkedList()
    current = llist_1.head
    
    resultant = result.head
    while current:
        if not result.has(current.value):
            result.append(current.value)
        current = current.next
    
    while resultant:
        if not llist_2.has(resultant.value):
            result.append(resultant.value)
        resultant = resultant.head
    return result

# Test case 1

""" linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4)) """

    






