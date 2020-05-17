# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Microsoft.
#
# You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board
# where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row,
# column, or diagonal.
# GG: decent review of backtracking
from copy import deepcopy


def is_valid(n: int, qs: list) -> bool:
    # check if any pairs are on same diagonal in O(n^2)
    for r1, c1 in enumerate(qs):
        for r2, c2 in enumerate(qs):
            if r1 != r2 and abs(r1 - r2) == abs(c1 - c2):
                return False
    return True


def find_num_n_queen(n: int) -> int:
    solutions = []  # this will be list of lists

    def n_queen_solver(qs: list):
        if len(qs) == n:
            one_sol = deepcopy(qs)
            solutions.append(one_sol)

        possible_cols = [x for x in range(n) if x not in qs]  # slight optimization, since queens can't be on same cols.
        possible_cols = possible_cols if len(qs) == 0 else [pc for pc in possible_cols if
                                                            pc != qs[-1] + 1 and pc != qs[-1] - 1]
        for c in possible_cols:
            qs.append(c)
            if is_valid(n, qs):
                n_queen_solver(qs)

            qs.pop()  # backtracking

    n_queen_solver([])
    return len(solutions)


# SEE https://math.stackexchange.com/questions/1872444/how-many-solutions-are-there-to-an-n-by-n-queens-problem
assert find_num_n_queen(1) == 1
assert find_num_n_queen(2) == 0
assert find_num_n_queen(3) == 0
assert find_num_n_queen(4) == 2
assert find_num_n_queen(5) == 10
assert find_num_n_queen(6) == 4
assert find_num_n_queen(7) == 40
assert find_num_n_queen(8) == 92
assert find_num_n_queen(9) == 352
assert find_num_n_queen(10) == 724
