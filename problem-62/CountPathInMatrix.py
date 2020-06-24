# This problem was asked by Facebook.
#
# There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the
# top-left corner and getting to the bottom-right corner. You can only move right or down.
#
# For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:
#
# Right, then down
# Down, then right
# Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.

import math


def count_num_paths_dp(n: int, m: int) -> int:
    # GG: interesting case where dynamic programming problem has a math solution.
    if n == 0 or m == 0:
        return 0
    if n == 1 or m == 1:
        return 1

    memo = [[0 for _ in range(m)] for _ in range(n)]
    memo[0][0] = 1
    # print(n)
    # print(m)
    # print(memo)

    for i in range(n):
        for j in range(m):
            if i == j == 0:
                continue
            from_left = memo[i][j - 1] if j > 0 else 0
            from_up = memo[i - 1][j] if i > 0 else 0
            memo[i][j] = from_up + from_left

    return memo[-1][-1]


assert count_num_paths_dp(0, 0) == 0
assert count_num_paths_dp(1, 5) == 1
assert count_num_paths_dp(7, 1) == 1
assert count_num_paths_dp(2, 2) == 2
assert count_num_paths_dp(5, 5, ) == 70


def count_num_paths_math(n: int, m: int) -> int:
    # TBC: try doing the math nCm way
    if n == 0 or m == 0:
        return 0
    if n == 1 or m == 1:
        return 1

    return math.factorial(n - 1 + m - 1) // (math.factorial(n - 1) * math.factorial(m - 1))


assert count_num_paths_math(0, 0) == 0
assert count_num_paths_math(1, 5) == 1
assert count_num_paths_math(9, 1) == 1
assert count_num_paths_math(2, 2) == 2
assert count_num_paths_math(5, 5) == 70
