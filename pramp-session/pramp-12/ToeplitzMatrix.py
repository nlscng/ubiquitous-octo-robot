# Toeplitz Matrix A Toeplitz matrix is a matrix where every left-to-right-descending diagonal has the same element.
# Given a non-empty matrix arr, write a function that returns true if and only if it is a Toeplitz matrix. The matrix
# can be any dimensions, not necessarily square.
#
# For example,
#
# [[1,2,3,4],
#  [5,1,2,3],
#  [6,5,1,2]]
# is a Toeplitz matrix, so we should return true, while
#
# [[1,2,3,4],
#  [5,1,9,3],
#  [6,5,1,2]]
# isn’t a Toeplitz matrix, so we should return false.


def is_toeplitz(matrix: list):
    if not matrix or len(matrix) < 2 or len(matrix[0]) < 2:
        return True

    nr, nc = len(matrix), len(matrix[0])  # num of row, num of col
    for i in range(1, nr):
        for j in range(1, nc):
            if matrix[i][j] != matrix[i - 1][j - 1]:
                return False
    return True


assert is_toeplitz([[4, 0], [9, 4]])
assert is_toeplitz([[6, 4, 4]])
assert is_toeplitz([[3], [5], [6]])
assert is_toeplitz([[3, 9], [5, 3], [6, 5]])
assert not is_toeplitz([[3, 1, 7], [4, 1, 1], [2, 4, 3]])
assert not is_toeplitz([[8, 8, 8, 8, 8], [8, 8, 8, 8, 9], [8, 8, 8, 8, 8], [8, 8, 8, 8, 8], [8, 8, 8, 8, 8]])
