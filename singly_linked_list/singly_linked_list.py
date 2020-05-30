import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import ListNode

class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0
        
    def __len__(self):
        return self.length
    
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        
        if not self.tail:
            self.head = self.tail = new_node
                       
        else:
            current_tail = self.tail
            current_tail.next = new_node
            current_tail.next.prev = current_tail
            self.tail = new_node
    
    def contains(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.value != value:
                current_node = current_node.next
            else:
                return True
        
        return False
        
    def remove_head(self):
        if not self.head:
            return
        
        value = self.head.value
        if self.head == self.tail:
            self.head = self.tail = None
            
        else:
            self.head = self.head.next
            self.head.prev = None 

        self.length -= 1
        return value
    
    def get_max(self):
        if not self.head:
            return
                
        current_node = self.head
        current_max = current_node.value
        
        while current_node is not None:
            if current_node.value > current_max:
                current_max = current_node.value
            
            current_node = current_node.next
        return current_max
                