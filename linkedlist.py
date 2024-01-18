class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    #represents a node in the linked list. Each node contains a data attribute to store the actual data and a next attribute to point to the next node in the list.

class LinkedList:
    def __init__(self):
        self.head = None
    #represents the linked list itself. It has a head attribute that points to the first node in the list.

    def append(self, data): #add new nodes to the end of the list.
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def remove_dup(self): #removes duplicates from the linked list. It does this by iterating through the list, checking if the data in the current node matches the data in the next node, and then adjusting the pointers to skip over duplicate nodes.
        if not self.head:
            return
        current = self.head
        while current:
            data = current.data
            prev_node = current
            current = current.next
            while current and current.data == data:
                current = current.next
            prev_node.next = current
        
    def remove(self, value): #removes a node with a specific value from the linked list, checks whether the node to be removed is the head node or a non-head node and handles the removal accordingly.
        if not self.head:
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next

    def display(self): #used to print the elements of the linked list sequentially.
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
