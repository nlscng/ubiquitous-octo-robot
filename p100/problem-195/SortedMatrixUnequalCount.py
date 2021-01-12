# This problem was asked by Google.
#
# Let A be an N by M matrix in which every row and every column is sorted.
#
# Given i1, j1, i2, and j2, compute the number of elements of M smaller than M[i1, j1] and larger than M[i2, j2].
#
# For example, given the following matrix:
#
# [[1, 3, 7, 10, 15, 20],
#  [2, 6, 9, 14, 22, 25],
#  [3, 8, 10, 15, 25, 30],
#  [10, 11, 12, 23, 30, 35],
#  [20, 25, 30, 35, 40, 45]]
# And i1 = 1, j1 = 1, i2 = 3, j2 = 3, return 15 as there are 15 numbers in the matrix smaller than 6 or greater than 23.

"""
The naive brute force way to doing this is have two, nested, for loops and just scan every element. The big O for that
is O(n*m), where n is num of row, m is num of col.

Slight modification is, with one for loop, spin through all the rows, and run binary search for num of elements smaller
than k. This will be O(n * log(m)).

Or, break this down into two questions, one for number of elements smaller than, the other for number larger than.

Each one of them can be solved by some type of walking. For the smaller than, I can walk from last row back up,
eliminating a row if first index has value greater than our target. If it's smaller, I walk right til I find one bigger,
and I'd know how many elements are smaller/bigger than target on this row, etc.

This should be O(n + m)
"""

##Google
##SortedMatrix

from typing import List


def count_smaller_sorted_matrix(matrix: List[List[int]], k: int) -> int:
    assert matrix and matrix[0]

    n = len(matrix)
    m = len(matrix[0])

    r, c = n - 1, 0
    count = 0

    while r >= 0 and c < m:
        walker = matrix[r][c]
        if walker < k:
            c += 1
        else:  # walker >= k
            r -= 1
            count += c

    if r >= 0:
        count += (r + 1) * m

    return count


t1 = [[1, 4, 8],
      [2, 10, 13],
      [5, 18, 19]]
assert count_smaller_sorted_matrix(t1, 7) == 4
assert count_smaller_sorted_matrix(t1, 15) == 7
assert count_smaller_sorted_matrix(t1, 1) == 0
assert count_smaller_sorted_matrix(t1, 20) == 9


def count_greater_sorted_matrix(matrix: List[List[int]], k: int) -> int:
    #TBC
    pass