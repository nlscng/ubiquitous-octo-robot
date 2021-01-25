# This problem was asked by Google.
#
# Given a set of distinct positive integers, find the largest subset such that every pair of elements in the subset (
# i, j) satisfies either i % j = 0 or j % i = 0.
#
# For example, given the set [3, 5, 10, 20, 21], you should return [5, 10, 20]. Given [1, 3, 6, 24], return [1, 3, 6,
# 24].

##Google
##SubsetSum
##DP
##DynamicProgramming

"""
This feels like a dp problem of a 2D memo table. I can have a table where both
the row and the column represent an element in the array, and have the cell
record a boolean for if the r and c value are mutually divisible.

This would be O(n^2) in time and space.

After googling, we can apparently reduce the space to O(n), by counting on the fact
that smaller divisor will be divide up larger divisible numbers. Essentially treat
this as a LIS DP problem, where condition add one to the number of the subset is
where or not two values are mutually divisible.
"""

from typing import List


def mutually_divisible(a: int, b: int) -> bool:
    return a % b == 0 if a >= b else b % a == 0


def largest_divisible_subset(lis: List[int]) -> List[int]:
    # This involves a sort at first to help the divisibility test, so that's
    # O(n log n) in time. And I have a for loop with a max function to scan, so
    # that's O(n^2) in time. The memo table is 1D, so O(n) in space. And at the end
    # I did another scan to pick up the elements in this largest group, so another
    # O(n) in time.
    # Overall this is O(n^2) in time and O(n) in space
    assert lis
    lis.sort()  # this makes this function non pure
    n = len(lis)
    memo = [0] * n   # each cell at i-th is to keep counts of number of divisible members that includes value at i-th
    memo[0] = 1
    for i in range(1, n):
        div_able_count = [memo[x] for x in range(0, i) if mutually_divisible(lis[x], lis[i])]
        if len(div_able_count) > 0:
            memo[i] = max(div_able_count) + 1
        else:
            memo[i] = 1

    largest_idx = memo.index(max(memo))
    return [x for x in lis if mutually_divisible(x, lis[largest_idx])]


assert largest_divisible_subset([3, 5, 10, 20, 21]) == [5, 10, 20]
assert largest_divisible_subset([1, 3, 6, 24]) == [1, 3, 6, 24]
