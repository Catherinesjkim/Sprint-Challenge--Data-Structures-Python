"""
Task 3. Reverse a Linked List
Inside of the reverse directory, you'll find a basic implementation of a Singly Linked List. Without making it a Doubly Linked List (adding a tail attribute), complete the reverse_list() function within reverse/reverse.py.

Time Complextity: O(n)
Space Complexity: O(1)
"""

class Node:
    # constructor to initialize the node object
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    # function to initialize the head node
    def __init__(self):
        self.head = None

    # function to insert a new node at the beginning
    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    # function to search through the LL
    # constains == true or false
    def contains(self, value):
        if not self.head:
            return False
        
        # loop through each node, until we see the value ,or we cannot go further
        current = self.head

        while current:
            # check if this is the node we are looking for
            if current.get_value() == value:
                return True

            # otherwise, go to the next node
            current = current.get_next()

        return False

    # catherine's code
    # function to reverse the LL 
    # initialize three pointers: prev as NULL, current as head and next as NULL
    def reverse_list(self, x=None, y=None): # replaced 'node and 'prev' to meet my test's requirements
        if self.head == None:
            return None
        current = self.head
        prev = None
        
        # iterate through the LL. In loop, do the following:
        while current != None:
            # before changing next of current, store next node 
            next = current.next_node
            
            # now change next of current - this is where the actual reversing happens
            current.next_node = prev
            
            # move prev and current one step forward
            prev = current
            current = next
            
        self.head = prev
        
    # Utility function to print the linked LinkedList
    def print_list(self):
        current = self.head
        while(current):
            print(current.value)
            current = current.next_node

# print out the results of the methods
linked_list = LinkedList()

linked_list.add_to_head(0)
print(f'Does our LL contain 0? {linked_list.contains(0)}')
print(f'Does our LL contain 1? {linked_list.contains(1)}')

linked_list.add_to_head(2)
print(f'The start of the list is {linked_list.head.value}')

linked_list.add_to_head(5)
print(f'The start of the list is {linked_list.head.value}')

print(f'Given Linked List:')
linked_list.print_list()

linked_list.reverse_list()
print(f'Reversed Linked List: ')
linked_list.print_list()
        
