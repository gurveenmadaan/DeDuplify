from linkedlist import Node, LinkedList #imports the Node and LinkedList classes from the linkedlist.py. These classes are used to construct linked lists, which are used within the hash set.

class HashSet: #represents a hash set using separate chaining
    def __init__(self, size):
        #takes the initial size of the hash set as an argument and initializes size(The number of buckets in the hash set.) and buckets (array to store linked lists, where each list represents a bucket.)
        self.size = size
        self.buckets = [None] * size
    # "bucket" refers to a container or slot where elements with the same hash value are stored. Each bucket can hold one or more elements that have been hashed to the same index in the hash table or hash set.
    def hash_function(self, value): #calculates the hash value
        return hash(value) % self.size
    
    def add(self, value):
        #calculates the index for the value using the hash_function. If the bucket at that index is None, it initializes a new linked list and assigns it to the bucket. It then appends the value to the linked list at the calculated index.
        index = self.hash_function(value)
        if self.buckets[index] is None: 
            self.buckets[index] = LinkedList()
        linkedlist = self.buckets[index]
        linkedlist.append(value)
    
    def remove_dupes(self):
        #goes through each bucket in the hash set and removes duplicates from the linked list in each bucket.
        for linkedlist in self.buckets:
            if linkedlist:
                linkedlist.remove_dup()

                unique_values = set()
                current = linkedlist.head
                while current.next:
                    if current.next.data in unique_values:
                        current.next = current.next.next
                    else:
                        unique_values.add(current.next.data)
                        current = current.next
