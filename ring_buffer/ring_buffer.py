# Task 1. Implement a Ring Buffer or Circular Queue Data Structure

# define a buffer with a fixed size, so that when it fills up, adding another element must overwrite the first (oldest) one. 

# a ring buffer doesn't get a head or tail, just a size (capacity) and an empty buffer/array
class RingBuffer:
    # class that implements a not-yet-full buffer
    def __init__(self, capacity):
        self.capacity = capacity # size/count
        self.buffer = [] # empty array - obj
        self.current = 0

    def append(self, item):
        # append an element overwriting the oldest one 
        if len(self.buffer) < self.capacity:
            self.buffer.append(item)
        elif len(self.buffer) == self.capacity:
            self.buffer[self.current] = item
            self.current = (self.current + 1) % self.capacity
        # return the item at the front/head of the line and remove it
        # not actually removing an item from the array, it's just increasing the head to point at the next item "in line"

    def get(self):
        # return a list of elements from the oldest to the newest
        if self.buffer is not None:
            return self.buffer[:self.current]+self.buffer[self.current:]
        
# test
bufferT = RingBuffer(3)

bufferT.get() # should return []
print(f'The Initial Ring Buffer: {bufferT.buffer}')

bufferT.append('a')
bufferT.append('b')
bufferT.append('c')

bufferT.get() # should return ['a', 'b', 'c']
print(f'Output of the full Ring Buffer: {bufferT.buffer}')

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
bufferT.append('d')
bufferT.get() # should return ['d', 'b', 'c']
print(f'Output the Ring Buffer with appended d: {bufferT.buffer}')

bufferT.append('e')
bufferT.append('f')
bufferT.get() # should return ['d', 'e', 'f']
print(f'Output the Ring Buffer with appneded e and f: {bufferT.buffer}')