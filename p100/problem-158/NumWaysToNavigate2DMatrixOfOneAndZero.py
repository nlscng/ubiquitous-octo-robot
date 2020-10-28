# This problem was asked by Slack.
#
# You are given an N by M matrix of 0s and 1s. Starting from the top left corner, how many ways are there to reach
# the bottom right corner?
#
# You can only move right and down. 0 represents an empty space while 1 represents a wall you cannot walk through.
#
# For example, given the following matrix:
#
# [[0, 0, 1],
#  [0, 0, 1],
#  [1, 0, 0]]
# Return two, as there are only two ways to get to the bottom right:
#
# Right, down, down, right
# Down, right, down, right
# The top left corner and bottom right corner will always be 0.

"""
If this weren't of zeros and ones, it'd be a simple math problem, basically num of ways of permutation for left and
down til the bottom right corner.

As is, I feel like a dynamic programming should solve this, if not an overkill.


"""


def num_paths(matrix: list) -> int:
    assert matrix and matrix[0]

    n = len(matrix)
    m = len(matrix[0])

    memo = [[0 for _ in range(m)] for _ in range(n)]
    memo[0][0] = 1
    for r in range(n):
        for c in range(m):
            if r == c == 0:
                continue
            elif matrix[r][c] == 0:
                from_top = memo[r - 1][c] if r > 0 and matrix[r - 1][c] == 0 else 0
                from_left = memo[r][c - 1] if c > 0 and matrix[r][c - 1] == 0 else 0
                memo[r][c] = from_top + from_left
    return memo[-1][-1]


matrix_a = [[0, 0, 1],
            [0, 0, 1],
            [1, 0, 0]]
assert num_paths(matrix_a) == 2

matrix_b = [[0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0]]
assert num_paths(matrix_b) == 3
matrix_c = [[0, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
assert num_paths(matrix_c) == 8
