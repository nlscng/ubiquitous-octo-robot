# This question was asked by Zillow.
#
# You are given a 2-d matrix where each cell represents number of coins in that cell. Assuming we start at matrix[0][0], and can only move right or down, find the maximum number of coins you can collect by the bottom right corner.
#
# For example, in this matrix
#
# 0 3 1 1
# 2 0 0 4
# 1 5 3 1
# The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.


"""
Another dp problem, and one that's very similar to value iteration

I can only go down or right, which means, a cell will get its sum from up or left. This is how the memo table
should be filled

"""


def collect_max(matrix: list) -> int:
    if not matrix:
        return 0

    row = len(matrix)
    col = len(matrix[0])

    # memo = [[0 for _ in range(col)] for _ in range(row)]

    for r in range(row):
        for c in range(col):
            from_left = matrix[r][c - 1] if c > 0 else 0
            from_top = matrix[r - 1][c] if r > 0 else 0
            matrix[r][c] = matrix[r][c] + max(from_left, from_top)

    return matrix[row - 1][col - 1]


t = [[0, 3, 1, 1], [2, 0, 0, 4], [1, 5, 3, 1]]
assert collect_max(t) == 12

t = [[1, 3, 1, 1], [2, 0, 0, 4], [1, 5, 3, 1]]
assert collect_max(t) == 13

t = [[0, 3, 1, 1], [2, 3, 1, 4], [1, 5, 3, 1]]
assert collect_max(t) == 15

t = [[0, 3, -1, 1], [2, -1, 3, 4], [1, 5, -3, 1]]
assert collect_max(t) == 10



