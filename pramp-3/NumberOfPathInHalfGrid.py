# You’re testing a new driverless car that is located at the Southwest (bottom-left) corner of an n×n grid. The car
# is supposed to get to the opposite, Northeast (top-right), corner of the grid. Given n, the size of the grid’s
# axes, write a function numOfPathsToDest that returns the number of the possible paths the driverless car can take.

#
# For convenience, let’s represent every square in the grid as a pair (i,j). The first coordinate in the pair denotes
# the east-to-west axis, and the second coordinate denotes the south-to-north axis. The initial state of the car is (
# 0,0), and the destination is (n-1,n-1).
#
# The car must abide by the following two rules: it cannot cross the diagonal border. In other words, in every step
# the position (i,j) needs to maintain i >= j. See the illustration above for n = 5. In every step, it may go one
# square North (up), or one square East (right), but not both. E.g. if the car is at (3,1), it may go to (3,2) or (4,
# 1).
#
# Explain the correctness of your function, and analyze its time and space complexities.


def num_of_paths_to_dest(n):
    table = [[0] * (n + 1) for _ in range(n + 1)]

    ## init
    table[1][1] = 1
    for i in range(len(table[0])):
        table[0][i] = 0
    for i in range(len(table[0])):
        table[i][0] = 0

    for i in range(1, n + 1):
        for j in range(2, n + 1):
            if i > j:
                pass
            elif i == j:
                table[i][j] = table[i - 1][j]
            else:
                table[i][j] = table[i - 1][j] + table[i][j - 1]

    return table[n][n]


assert num_of_paths_to_dest(1) == 1
assert num_of_paths_to_dest(2) == 1
assert num_of_paths_to_dest(3) == 2
assert num_of_paths_to_dest(4) == 5
assert num_of_paths_to_dest(6) == 42
assert num_of_paths_to_dest(17) == 35357670
