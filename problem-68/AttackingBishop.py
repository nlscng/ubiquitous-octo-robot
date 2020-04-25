# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# On our special chessboard, two bishops attack each other if they share the same diagonal. This includes bishops
# that have another bishop located between them, i.e. bishops can attack through pieces.
#
# You are given N bishops, represented as (row, column) tuples on a M by M chessboard. Write a function to count the
# number of pairs of bishops that attack each other. The ordering of the pair doesn't matter: (1, 2) is considered
# the same as (2, 1).
#
# For example, given M = 5 and the list of bishops:
#
# (0, 0)
# (1, 2)
# (2, 2)
# (4, 0)
# The board would look like this:
#
# [b 0 0 0 0]
# [0 0 b 0 0]
# [0 0 b 0 0]
# [0 0 0 0 0]
# [b 0 0 0 0]
# You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.


def find_attacking_bishops(board_width: int, bishop_locs: list):
    count = 0
    for i in range(len(bishop_locs)):
        for j in range(i+1, len(bishop_locs)):
            if abs(bishop_locs[i][0] - bishop_locs[j][0]) == abs(bishop_locs[i][1] - bishop_locs[j][1]):
                count += 1

    return count


assert find_attacking_bishops(5, [(0, 0), (1, 2), (2, 2)]) == 1, \
    "actual: {}".format(find_attacking_bishops(5, [(0, 0), (1, 2), (2, 2)]))
assert find_attacking_bishops(5, [(0,0), (1,2), (2,2), (4,0)]) == 2, \
    "actual: {}".format(find_attacking_bishops(5, [(0,0), (1,2), (2,2), (4,0)]))
