"""
There are 2 text files containing 10,000 names each and a program names.py that compares the 2 files and prints out dupe name entries. 

Six seconds is an eternity so you've been tasked with speeding up the code. Your goal is to use one of the data structures we built out over the course of this week in order to optimize and improve on the runtime so that it's more efficient than O(n²).

What other data structures (including ones from Python's standard library) are also possible candidates for improving the runtime of the implementation?
"""

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    # insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
                
        # Return True if the tree contains the value
        # False if it does not 
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)
                
# runtime: 0.11209893226623535 seconds
# used binary search tree (BST) to optimize the runtime
# Average: Logarithmic O(log n) - as the size of the input increases, the runtime or space used will grow at a slightly slower rate.
# Worst: Linear O(n) - as the size of the input increases, the runtime or space used will grow at the same rate

# We can also use Python's Built-in Sort Functions
# sort()
