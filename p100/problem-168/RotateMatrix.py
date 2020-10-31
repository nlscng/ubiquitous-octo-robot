# This problem was asked by Facebook.
#
# Given an N by N matrix, rotate it by 90 degrees clockwise.
#
# For example, given the following matrix:

"""
This is about indices manipulation, and should be able to do it in-place in python.

0,0  0,1  0,2

1,0  1,1  1,2

2,0  2,1  2,2

0,0 => 0,2
0,1 => 1,2
0,2 => 2,2
1,1 => 1,0
1,0 => 0,1
1,2 => 2,1
2,0 => 0,0

So this should be looked at with a center of the matrix (take care for both cases, if matrix is even width or odd width)

given a cell, let dr be row-wise distance from that cell to center, dc be column-wise distance from center. Then this
cell should be rotated by switching dx with dy, adjusting signs for either or both of them to get proper rotation


"""


def rotate_cell(r: int, c: int, m: list):
    w, h = len(m[0]), len(m)
    assert 0 <= r < w and 0 <= c < h and w == h
    cr, cc = (w - 1) / 2, (h - 1) / 2  # center row, center column
    dr, dc = cr - r, cc - c  # delta in rows, delta in columns

    m[int(cr - dr)][int(cc - dc)], m[int(cr - dc)][int(cc + dr)] = m[int(cr - dc)][int(cc + dr)], m[int(cr - dr)][
        int(cc - dc)]
    m[int(cr - dr)][int(cc - dc)], m[int(cr + dr)][int(cc + dc)] = m[int(cr + dr)][int(cc + dc)], m[int(cr - dr)][
        int(cc - dc)]
    m[int(cr - dr)][int(cc - dc)], m[int(cr + dc)][int(cc - dr)] = m[int(cr + dc)][int(cc - dr)], m[int(cr - dr)][
        int(cc - dc)]


# m1 = [[1, 2],
#       [4, 3]]
#
# rotate_cell(0, 0, m1)
# assert m1 == [[4, 1], [3, 2]]
#
# m2 = [[1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9]]
# rotate_cell(0, 0, m2)
# rotate_cell(0, 1, m2)
# assert m2 == [[7, 4, 1],
#               [8, 5, 2],
#               [9, 6, 3]]


def rotate_matrix(matrix: list):
    assert matrix
    w, h = len(matrix[0]), len(matrix)
    assert w == h

    # iterate over a quadrant, take note to skip one side of the quadrant, as they will be processed by the other side
    for r in range((w + 1) // 2):
        for c in range(h // 2):
            rotate_cell(r, c, matrix)

    return matrix


m1 = [[1, 2],
      [4, 3]]
rotate_matrix(m1)
assert m1 == [[4, 1], [3, 2]]

m2 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]
rotate_matrix(m2)
assert m2 == [[7, 4, 1],
              [8, 5, 2],
              [9, 6, 3]]

m3 = [[1, 2, 3, 4],
      [1, 2, 3, 4],
      [1, 2, 3, 4],
      [1, 2, 3, 4]]
rotate_matrix(m3)
assert m3 == [[1, 1, 1, 1],
              [2, 2, 2, 2],
              [3, 3, 3, 3],
              [4, 4, 4, 4]]
