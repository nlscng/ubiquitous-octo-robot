# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.
#
# Given N, write a function to return the number of knight's tours on an N by N chessboard.

EMPTY = 0
VISITED = 1

def print_board(board: list):
    for x in range(len(board)):
        for y in range(len(board[0])):
            val = board[x][y]


def is_valid_move(x, y, n, board: list) -> bool:
    return 0 <= x < n and 0 <= y < n and board[x][y] == EMPTY


def valid_next_moves(x: int, y: int, n: int, board: list) -> list:
    moves = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
    res = []
    for x_delta, y_delta in moves:
        next_x = x + x_delta
        next_y = y + y_delta
        if is_valid_move(next_x, next_y, n, board):
            res.append((next_x, next_y))
    return res


def found_a_tour(board) -> bool:
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                return False
    return True


def knights_tour(n: int, start_x: int = 0, start_y: int = 0) -> int:
    # solutions = []  # list of tuple for coordinates
    num_sol = [0]
    board = [[EMPTY] * n for _ in range(n)]
    assert len(board) == n and len(board[0]) == n
    board[start_x][start_y] = VISITED

    def explore_recur(x, y):
        if found_a_tour(board):
            num_sol[0] += 1
            return

        for next_x, next_y in valid_next_moves(x, y, n, board):
            board[next_x][next_y] = VISITED
            explore_recur(next_x, next_y)
            board[next_x][next_y] = EMPTY   # backtrack

    explore_recur(start_x, start_y)

    return num_sol[0]


assert knights_tour(1) == 1
assert knights_tour(2) == 0
assert knights_tour(3) == 0
assert knights_tour(4) == 0
res_5 = knights_tour(5)
assert res_5 == 304, "Actual: {}".format(res_5)
res_5 = knights_tour(5, start_x=0, start_y=1)
assert res_5 == 0, "Actual: {}".format(res_5)
