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

# GG: So there are many other ways to do this with linear space. I could
#   use a dictionary and keeps a mapping of value and their respective new index,
#   or like I was using a queue.
#   One way to do this with constant space, but O(n*k) time, is to rotate
#   the whole array one element k times.
#   To do this with constant space, a version of it is to reverse it a few times.
#   Like abcde, we want to rotate right by 3, to cdeab
#   We start reverse everything, edcba
#   and we reverse in place, the old k+ units, the now first k+ unit, to cdeba
#   then we reverse the old first k units, the now k+ units, to cdeab

# REF: https://www.geeksforgeeks.org/array-rotation/

# assert array_rotate_right([1, 2, 3, 4, 5], 1) == [2, 3, 4, 5, 1]
# assert array_rotate_right([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]
# assert array_rotate_right([1, 2, 3, 4, 5], 3) == [4, 5, 1, 2, 3], "Actual: {}".format(
#     array_rotate_right([1, 2, 3, 4, 5], 3))
# assert array_rotate_right([1, 2, 3, 4, 5], 4) == [5, 1, 2, 3, 4], "Actual: {}".format(
#     array_rotate_right([1, 2, 3, 4, 5], 4))
