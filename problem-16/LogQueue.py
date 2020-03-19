# You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to
# accomplish this, with the following API:
#
# record(order_id): adds the order_id to the log get_last(i): gets the ith last element from the log. i is guaranteed
# to be smaller than or equal to N. You should be as efficient with tiYou run an e-commerce website and want to
# record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:
#
# record(order_id): adds the order_id to the log
# get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
# You should be as efficient with time and space as possible

from collections import deque


class LogQueue:
    def __init__(self, capacity: int):
        self.log = []
        self.capacity = capacity

    def record(self, order_id: int):
        if len(self.log) == self.capacity:
            self.log = self.log[1:]

        if len(self.log) < self.capacity:
            self.log.append(order_id)

    def get_last(self, i: int):
        assert i < self.capacity
        idx_old = self.capacity - i
        out = self.log[idx_old]
        return out


log = LogQueue(5)
log.record(1)
log.record(2)
assert log.log == [1, 2]
log.record(3)
log.record(4)
log.record(5)
assert log.log == [1, 2, 3, 4, 5]
log.record(6)
log.record(7)
log.record(8)
assert log.log == [4, 5, 6, 7, 8]
assert log.get_last(4) == 5
assert log.get_last(1) == 8
