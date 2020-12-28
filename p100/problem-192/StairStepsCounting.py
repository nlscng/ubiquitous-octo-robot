# This problem was asked by Google.
#
# You are given an array of nonnegative integers. Let's say you start at the beginning of the array and are trying to
# advance to the end. You can advance at most, the number of steps that you're currently on. Determine whether you
# can get to the end of the array.
#
# For example, given the array [1, 3, 1, 2, 0, 1], we can go from indices 0 -> 1 -> 3 -> 5, so return true.
#
# Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.

"""This is another flavor of reaching the top of stairs problem, I think. Which means it should be solvable with
dynamic programming

I think a 1-D array of boolean should be enough.
Let P(i) be if the i-th step/index is reachable from the beginning of the array
then P(i) = True if P(i - V(i)) is True, where V(i) is a range of value 0 <= value of element of i-th index,
otherwise False.

Then we return the last element of P
"""

##Google
##DP
##DynamicProgramming

from typing import List


def step_counting(lis: List[int]):
    # this version is O(n * v) in time and O(n) in space, where n is length of the list and v is max value of elements
    # in the list; maybe there's a way to do this with O(n) in time
    assert lis
    assert all([x >= 0 for x in lis])

    n = len(lis)
    p = [False for _ in range(n)]
    p[0] = True if lis[0] > 0 else False

    for i in range(n):
        if p[i]:
            vi = lis[i]
            if vi > 0:
                # GG: it's critical to spin from 1 to vi + 1, as we want to test for the value of v too, not 0 ~ v-1
                for v in range(1, vi + 1):
                    if i + v < n:
                        p[i + v] = True

    return p[n - 1]


assert step_counting([1, 3, 1, 2, 0, 1])
assert step_counting([3, 0, 0, 0])
assert not step_counting([0, 1, 2, 3, 2])
assert not step_counting([1, 2, 1, 0, 0])
