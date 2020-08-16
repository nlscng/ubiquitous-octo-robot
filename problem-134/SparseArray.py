# This problem was asked by Facebook.
#
# You have a large array with most of the elements as zero.
#
# Use a more space-efficient data structure, SparseArray, that implements the same interface:
#
# init(arr, size): initialize with the original large array and size.
# set(i, val): updates index at i with val.
# get(i): gets the value at index i.

"""
This should be pretty easy, I am thinking a map could do it, where key is the index pointing at value of the element
"""


# GG: I think this is a great question for clarification questions: such as can this array contain null or none
#  or if we can default value to zero, etc

class SparseArray:
    def __init__(self, arr: list, size: int):
        assert len(arr) == size
        self.memo = {k: v for k, v in enumerate(arr) if k != 0}
        self.size = size

    def set(self, i: int, v):
        if self.size < i:
            self.size = i + 1
        self.memo[i] = v

    def get(self, i):
        if i >= self.size:
            raise IndexError("Index out of bound: {}".format(i))

        return self.memo[i] if i < self.size else 0


test = SparseArray([0, 0, 0, 0, 0, 0, 0, 42], 8)
assert test.get(4) == 0
assert test.get(7) == 42
test.set(42, 42)
assert test.get(42) == 42
