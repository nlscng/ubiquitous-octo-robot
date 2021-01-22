# This problem was asked by Amazon.
#
# Given an array and a number k that's smaller than the length of the array, rotate the array to the right k elements
# in-place.

"""
This smells like a two pointer problem.

Though naive solution is to do it with new array, to do this in place might involve
a queue, to preserve some elements. Or even better, maybe we can do it in place
without the extra space. Like swapping cards?

We will need a temp value holder, and the two walkers.

"""

from typing import List
from collections import deque


def array_rotate_right_linear_space(lis: List[int], k: int) -> List[int]:
    assert lis and 0 < k < len(lis)
    q = deque()
    f, s = k, 0
    while s < len(lis):
        q.append(lis[s])
        if f < len(lis):
            lis[s] = lis[f]
        else:
            v = q.popleft()
            lis[s] = v
        f += 1
        s += 1
    return lis


assert array_rotate_right_linear_space([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]
assert array_rotate_right_linear_space([1, 2, 3, 4, 5], 3) == [4, 5, 1, 2, 3]
assert array_rotate_right_linear_space([1, 2, 3, 4, 5], 4) == [5, 1, 2, 3, 4]

##TBC

# def array_rotate_right(lis: List[int], k: int) -> List[int]:
#     # GG: this is time of O(n) and space O(1)
#     assert lis and 0 < k < len(lis)
#
#     t = None  # temp value holder, initialized to the old head value
#     f, s = k, 0  # fast walker, slow walker
#
#     while f < len(lis):
#         lis[s], t, lis[f] = lis[f], lis[s], t
#         f += 1
#         s += 1
#     return lis
#
#
# assert array_rotate_right([1, 2, 3, 4, 5], 1) == [2, 3, 4, 5, 1]
# assert array_rotate_right([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]
# assert array_rotate_right([1, 2, 3, 4, 5], 3) == [4, 5, 1, 2, 3], "Actual: {}".format(
#     array_rotate_right([1, 2, 3, 4, 5], 3))
# assert array_rotate_right([1, 2, 3, 4, 5], 4) == [5, 1, 2, 3, 4], "Actual: {}".format(
#     array_rotate_right([1, 2, 3, 4, 5], 4))
