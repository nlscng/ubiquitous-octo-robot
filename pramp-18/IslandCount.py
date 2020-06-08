# Given a 2D array binaryMatrix of 0s and 1s, implement a function getNumberOfIslands that returns the number of
# islands of 1s in binaryMatrix.
#
# An island is defined as a group of adjacent values that are all 1s. A cell in binaryMatrix is considered adjacent
# to another cell if they are next to each either on the same row or column. Note that two values of 1 are not part
# of the same island if they’re sharing only a mutual “corner” (i.e. they are diagonally neighbors).


def get_number_of_islands(binaryMatrix):
    # safety check
    counter = 0  # number of groups of island, hack

    visited = set()

    def explore_and_mark(row, col, arr, visited):
        visited.add((row, col))  # mark this visited
        arr[row][col] = '*'
        # north
        if row > 0 and arr[row - 1][col] == 1 and (row - 1, col) not in visited:
            explore_and_mark(row - 1, col, arr, visited)

        # west
        if col > 0 and arr[row][col - 1] == 1 and (row, col - 1) not in visited:
            explore_and_mark(row, col - 1, arr, visited)

        # south
        if row < len(arr) - 1 and arr[row + 1][col] == 1 and (row + 1, col) not in visited:
            explore_and_mark(row + 1, col, arr, visited)

        # east
        if col < len(arr[0]) - 1 and arr[row][col + 1] == 1 and (row, col + 1) not in visited:
            explore_and_mark(row, col + 1, arr, visited)

    # spin through all cell
    for r in range(len(binaryMatrix)):
        for c in range(len(binaryMatrix[0])):
            if binaryMatrix[r][c] == 1:
                counter += 1
                explore_and_mark(r, c, binaryMatrix, visited)  # recursive visit ...

    return counter


assert get_number_of_islands([[0]]) == 0
assert get_number_of_islands([[1]]) == 1
assert get_number_of_islands([[1,0,1,0]]) == 2
assert get_number_of_islands([[1,0,1,0],[0,1,1,1],[0,0,1,0]]) == 2
assert get_number_of_islands([[1,0,1,0],[0,1,1,1],[0,0,1,0],[1,1,0,0],[0,1,0,1]]) == 4
assert get_number_of_islands([[0,1,0,1,0],[0,0,1,1,1],[1,0,0,1,0],[0,1,1,0,0],[1,0,1,0,1]]) == 6
assert get_number_of_islands([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]) == 1