# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Apple.
#
# Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the
# following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.
#

import copy


class OddQueue:
    def __init__(self):
        self.a = []
        self.b = []
        # self.capacity = capacity

    def enqueue(self, element):
        self.a.append(element)

    def dequeue(self):
        if len(self.b) == 0:
            self._refill()

        return self.b.pop() if len(self.b) > 0 else None

    def _refill(self):
        assert len(self.b) == 0
        self.b = self.a[::-1]
        self.a = []


my_q = OddQueue()
assert my_q.dequeue() is None

my_q.enqueue(0)
my_q.enqueue(1)
assert my_q.dequeue() == 0
assert my_q.dequeue() == 1

my_q.enqueue(0)
my_q.enqueue(1)
my_q.enqueue(2)
my_q.dequeue()  # 0
my_q.enqueue(3)
my_q.dequeue()  # 1
my_q.dequeue()  # 2
assert my_q.dequeue() == 3
