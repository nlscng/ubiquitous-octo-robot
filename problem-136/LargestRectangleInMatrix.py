# This question was asked by Google.
#
# Given an N by M matrix consisting only of 1's and 0's, find the largest rectangle containing only 1's and return its area.
#
# For example, given the following matrix:
#
# [[1, 0, 0, 0],
#  [1, 0, 1, 1],
#  [1, 0, 1, 1],
#  [0, 1, 0, 0]]
# Return 4.

# GG: I have no clue how to start this one on first look.

"""
1 0 0 0
1 0 1 1
1 0 1 1
0 1 0 0

{
1: 0
2: 1
3: 0
4: 0
}

1 0 1 0
1 0 1 1
1 0 0 1
0 1 0 0
{
1: 2
2: 0
3: 2
4: 1
}

1 0 1 1
1 1 1 1
1 1 1 1
0 1 0 0

1: 3
2: 2
3: 3
4: 3
"""

import sys


def largest_rect(matrix: list) -> int:
    assert len(matrix) > 0 and len(matrix[0]) > 0
    n = len(matrix)
    m = len(matrix[0])

    def cur_max_rect(count: dict) -> int:
        cur_max = 0
        cur_height = sys.maxsize
        cur_width = 0
        for k, v in count.items():
            if v != 0:
                cur_width += 1
                cur_height = min(cur_height, v)
                cur_max = max(cur_max, cur_height * cur_width, v)
            else:
                cur_width = 0
                cur_height = sys.maxsize
        return cur_max

    running_count = {k: 0 for k in range(m)}
    cur_max_area = 0
    for r in range(n):
        for c in range(m):
            if matrix[r][c] == 1:
                running_count[c] += 1
            else:
                running_count[c] = 0
        cur_max_area = max(cur_max_area, cur_max_rect(running_count))

    return cur_max_area


t = [[1, 0, 0, 0],
     [1, 0, 1, 1],
     [1, 0, 1, 1],
     [0, 1, 0, 0]]
assert largest_rect(t) == 4

s = [[1, 0, 1, 1],
     [1, 1, 1, 1],
     [1, 1, 1, 1],
     [0, 1, 0, 0]]
assert largest_rect(s) == 8

u = [[1, 0, 0, 0, 1],
     [1, 0, 1, 1, 1],
     [1, 1, 1, 0, 1],
     [0, 1, 0, 1, 1]]
assert largest_rect(u) == 4, "Actual: {}".format(largest_rect(u))

w = [[1, 0, 0, 0],
     [1, 0, 0, 1],
     [1, 0, 0, 1],
     [1, 1, 0, 0]]
assert largest_rect(w) == 4, "Actual: {}".format(largest_rect(w))

v = [[0, 0, 1, 1],
     [1, 1, 1, 1],
     [1, 0, 1, 1],
     [0, 1, 1, 1]]
assert largest_rect(v) == 8, "Actual: {}".format(largest_rect(v))
