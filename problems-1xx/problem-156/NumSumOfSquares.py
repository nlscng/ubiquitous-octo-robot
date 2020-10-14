# This problem was asked by Facebook.
#
# Given a positive integer n, find the smallest number of squared integers which sum to n.
#
# For example, given n = 13, return 2 since 13 = 32 + 22 = 9 + 4.
#
# Given n = 27, return 3 since 27 = 32 + 32 + 32 = 9 + 9 + 9.

"""
At first glance, this feels like a dynamic programming problem, like a coin exchange problem of unlimited number of
coins, where all the coins have face value of square.

k = 13
   1 2 3 4 5 6 7 8 9 10  11  12  13
1  1 2 3 4 ..
4  1 2 3 1 2 3 4 2 3 4   5   3
9  1 2 3 1 2 3 4 2 1 2   3   4   2
16

So let i be number-th coin involved, j be sum value of coins. Then c(i, j) =
{
    min of:
    c(i, j - v(c(i))) + 1, # using one coin of i, add v(c(i)) to get sum of j
    c(i - 1, v(c(i - 1)))  # don't use any i-th coin at all, either can't or won't use it, and still get to sum of j
}

n = 13
i = 2
0 1 2 3 4 5 6 7 8 9 10 11 12 13
0 1 2 3 1 2 3 4 2 9 10 11 12 13
"""

# GG: classic dynamic programming, coin change problem, this one with unlimited reuse of coin.
from math import ceil, sqrt

def min_num_sum_of_squares(n: int) -> int:
    # this is time O(n * m), where m is roughly square root of n, but space of O(n)
    if n < 4:
        return n

    ceiling = ceil(sqrt(n))
    # create a 1D memo table, where x is from 0 value to n
    memo = [i for i in range(n + 1)]
    for i in range(2, ceiling):
        for j in range(n + 1):
            value = i ** 2
            if j >= value:
                memo[j] = memo[j - value] + 1

    return memo[n]


assert min_num_sum_of_squares(13) == 2
assert min_num_sum_of_squares(27) == 3
assert min_num_sum_of_squares(42) == 4  # 16+16+9+1
