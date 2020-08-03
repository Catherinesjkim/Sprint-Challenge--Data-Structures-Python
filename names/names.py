# Task 2. Runtime Optimization
# Use one of the data structures we built out over the course of this week in order to optimize and improve ont he runtime so that's more efficient than O(n^2) == runtime: 5.286290884017944 seconds in my laptop

import time
from bst import BSTNode # import my improvements code file

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure
bst = BSTNode("Cat")

# Replace the nested for loops below with your improvements
for name_1 in names_1:
    bst.insert(name_1) # catherine's improvement
    
for name_2 in names_2:
    if name_2 not in duplicates:
        if bst.contains(name_2): # catherine's improvement
            duplicates.append(name_2)

end_time = time.time()

print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n") # 64 dupes

print(f"runtime: {end_time - start_time} seconds")
# runtime: 0.10244321823120117 seconds with BST 
# used binary search tree (BST) to optimize the runtime
# Average case: Logarithmic O(log n) faster - as the size of the input increases, the runtime or space used will grow at a slightly slower rate.
# Worst case: at leaset Linear O(n) faster - as the size of the input increases, the runtime or space used will grow at the same rate

# We can also use Python's Built-in Sort Functions
# sort()


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
