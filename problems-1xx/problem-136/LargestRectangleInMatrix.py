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

# GG: day 2, gave up trying to figure out myself, and found this is ultimately a variant of largest rectangle in
#  histogram problem

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

2,3,0,1,2
k, v: 1, 3
cur_max:
start idx: 0
max height: 2
"""


def largest_rect_histogram(count: []) -> int:
    # this is O(n) in time, and O(n) in space
    cur_max = 0
    idx_stack = []  # this will store indices, indicating potential starting point for a rectangle to calculate for.
    height_stack = []
    for idx, v in enumerate(count):
        if len(idx_stack) == 0 or v > height_stack[-1]:
            idx_stack.append(idx)
            height_stack.append(v)
        elif v < height_stack[-1]:
            # there are starting positions pushed into the stack already
            starting_idx = idx_stack[-1]
            while len(height_stack) > 0 and height_stack[-1] > v:
                starting_idx = idx_stack.pop()
                expiring_height = height_stack.pop()
                width = idx - starting_idx
                cur_max = max(cur_max, width * expiring_height)
            # GG: this next part is critical, you push back the starting idx for a next rectangle, which is your last popped
            idx_stack.append(starting_idx)
            height_stack.append(v)

    n = len(count)
    while len(idx_stack) > 0:
        starting_idx = idx_stack.pop()
        expiring_height = height_stack.pop()
        width = n - starting_idx
        cur_max = max(cur_max, width * expiring_height)
    return cur_max


assert largest_rect_histogram([2, 3, 0, 1, 2]) == 4
assert largest_rect_histogram([1, 2, 3, 1, 2]) == 5
assert largest_rect_histogram([1, 2, 4, 4]) == 8
assert largest_rect_histogram([3, 2, 3, 3]) == 8


def largest_rect(matrix: list) -> int:
    # let n be num of rows, m be number of cols, then this is O(n*m) in time and O(n*m) in space
    assert len(matrix) > 0 and len(matrix[0]) > 0
    n = len(matrix)
    m = len(matrix[0])

    running_count = [0 for _ in range(m)]
    cur_max_area = 0
    for r in range(n):
        for c in range(m):
            if matrix[r][c] == 1:
                running_count[c] += 1
            else:
                running_count[c] = 0
        cur_max_area = max(cur_max_area, largest_rect_histogram(running_count))

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
