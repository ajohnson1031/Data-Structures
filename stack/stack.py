import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

"""Queue implemented with List (Array) type:"""
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.insert(0, value)
        self.size += 1

    def pop(self):
        if not self.size:
            return 
        
        self.size -= 1
        return self.storage.pop(0)
    
"""Queue implemented with Linked List type:"""
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
        
    def __len__(self):
        return self.size
    
    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1
    
    def pop(self):
        if not self.size:
            return
        
        self.size -= 1
        return self.storage.remove_from_head()
        