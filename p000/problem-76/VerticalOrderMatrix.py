# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# You are given an N by M 2D matrix of lowercase letters. Determine the minimum number of columns that can be removed
# to ensure that each row is ordered from top to bottom lexicographically. That is, the letter at each column is
# lexicographically later as you go down each row. It does not matter whether each row itself is ordered
# lexicographically.
#
# For example, given the following table:
#
# cba
# daf
# ghi
# This is not ordered because of the a in the center. We can remove the second column to make it ordered:
#
# ca
# df
# gi
# So your function should return 1, since we only needed to remove 1 column.
#
# As another example, given the following table:
#
# abcdef
# Your function should return 0, since the rows are already ordered (there's only one row).
#
# As another example, given the following table:
#
# zyx
# wvu
# tsr
# Your function should return 3, since we would need to remove all the columns to order it.
'''
I guess this is the only optimization possible?
remaining char available < remaining height available: remove this col

row = 3
r = 1
'''


def vert_order_matrix(matrix: list) -> int:
    if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
        return 0

    row, col = len(matrix), len(matrix[0])
    count = 0
    for c in range(col):
        for r in range(1, row):
            if ord(matrix[r][c]) <= ord(matrix[r - 1][c]) or ord('z') - ord(matrix[r][c]) < row - r - 1:
                count += 1
                break

    return count


# assert vert_order_matrix([[]]) == 0
# assert vert_order_matrix([['a', 'b', 'c']]) == 0
# assert vert_order_matrix([['c', 'b', 'a'],
#                           ['d', 'a', 'f'],
#                           ['g', 'h', 'i']]) == 1
# assert vert_order_matrix([['z', 'y', 'x'],
#                           ['w', 'v', 'u'],
#                           ['t', 's', 'r']]) == 3
assert vert_order_matrix([['a', 'a', 'a'],
                          ['z', 'v', 'u'],
                          ['t', 's', 'r']]) == 3
