# This problem was asked by Microsoft.
#
# Given an array of positive integers, divide the array into two subsets such that the difference between the sum of
# the subsets is as small as possible.
#
# For example, given [5, 10, 15, 20, 25], return the sets {10, 25} and {5, 15, 20}, which has a difference of 5,
# which is the smallest possible difference.

"""
At first I thought this requires DP, like a subset sum problem. But maybe a sort and two pointers can solve this.

Turns out the naive, greedy, first approach solution, seems to work for simple cases, but fails over all. The
naive solution tries to minimize difference in any iteration, which fails to combine tiny number with big number to
compensate for medium numbers together.

Eg: [2, 3, 4, 5, 10]
"""
from typing import List


def min_diff_array_partition(liz: List[int]):
    assert liz and len(liz) > 1
    s_liz = sorted(liz)
    high, low = len(liz) - 1, 1
    high_sum, low_sum = s_liz[-1], s_liz[0]

    while high > low:
        if s_liz[low] + low_sum <= high_sum:
            low_sum += s_liz[low]
        else:
            high_sum += s_liz[low]
        low += 1

    return abs(high_sum - low_sum)


assert min_diff_array_partition([5, 10, 15, 20, 25]) == 5
assert min_diff_array_partition([0, 5, 1, 6]) == 0
assert min_diff_array_partition([2, 3, 4, 5, 10]) == 0
