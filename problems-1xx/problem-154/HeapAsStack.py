# This problem was asked by Amazon.
#
# Implement a stack API using only a heap. A stack implements the following methods:
#
# push(item), which adds an element to the stack
# pop(), which removes and returns the most recently added element (or throws an error if there is nothing on the stack)
# Recall that a heap has the following operations:
#
# push(item), which adds a new key to the heap
# pop(), which removes and returns the max value of the heap

"""
This looks straightforward, with the caveat of having to somehow maintain orders that's natural of a stack with
something while using the heap. I think one possible way to do that is just use tuple of (x, y), where x is the order
of push in stack, y is the actual item, and push (x, y) in the heap with x being the

"""

import heapq


class HeapAsStack:
    # GG: using a counter number to maintain order in the heap; since heap in python is min heap, the smallest number
    #  is kept at the top of the heap.
    def __init__(self):
        self.h = []  # internal list for heap storage
        self.counter = 0

    def push(self, item):
        internal_item = (self.counter, item)
        self.counter -= 1
        heapq.heappush(self.h, internal_item)

    def pop(self):
        (cur_counter, res) = heapq.heappop(self.h)
        assert cur_counter == self.counter + 1
        self.counter += 1
        return res


test_array = [32, 11, 91, 8, 51]
mock_stack = HeapAsStack()
for t in test_array:
    mock_stack.push(t)

mock_out = [mock_stack.pop() for _ in range(len(test_array))]
print(mock_out)

# note popping from a stack reverse the content of the stack
assert test_array == mock_out[::-1]
