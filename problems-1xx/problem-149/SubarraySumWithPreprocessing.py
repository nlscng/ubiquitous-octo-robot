# This problem was asked by Goldman Sachs.
#
# Given a list of numbers L, implement a method sum(i, j) which returns the sum from the sublist L[i:j] (including i,
# excluding j).
#
# For example, given L = [1, 2, 3, 4, 5], sum(1, 3) should return sum([2, 3]), which is 5.
#
# You can assume that you can do some pre-processing. sum() should be optimized over the pre-processing step.

"""
If I can preprocess the array into a lookup by two numbers, the actual sum() call could be of O(1).
Assuming we don't care about the complexity of processing, I can do a O(n^2) dictionary, where keys are all possible
pair of indices, and values are the subarray sum with it.

Or, this is from slight googling, with O(n), I can preprocess the array into another array, where each cell would hold
a sum from 0 to its index. And the sum() call would do two lookups with i and j, return the difference between the two.
This save preprocessing, but tiny bit of work on sum(), but still O(1)
"""

memo = {}


def subarray_sum(lis: list, i: int, j: int) -> int:
    assert lis and 0 <= i < j <= len(lis)
    n = len(lis)

    if not memo:
        for i in range(n):
            for j in range(n):
                memo[i, j] = sum(lis[i:j])

    return memo[i, j]


assert subarray_sum([1, 2, 3, 4, 5], 1, 1) == 2
assert subarray_sum([1, 2, 3, 4, 5], 0, 5) == 10
assert subarray_sum([1, 2, 3, 4, 5], 3, 5) == 9
