
import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.dll = DoublyLinkedList()
        self.count = len(self.dll)
        self.dict = {}
        

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        current_node = self.dll.head
        
        if key in self.dict:
            while key not in current_node.value and current_node.next is not None:
                current_node = current_node.next
                
            if key in current_node.value:
                self.dll.move_to_end(current_node)
                return current_node.value[key]
        
        return None
        

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        current_node = self.dll.head
        
        if key in self.dict.keys():
            self.dict[key] = value
            while current_node is not None:
                if key in current_node.value:       
                    current_node.value[key] = value
                
                current_node = current_node.next
            return
        
        if self.count >= self.limit:
            self.dll.remove_from_head()
            self.dll.add_to_tail({key: value})
            self.dict[key] = value
            
        else:
            self.count += 1
            self.dll.add_to_tail({key: value})
            self.dict[key] = value           
            
