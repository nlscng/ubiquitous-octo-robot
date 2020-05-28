# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.
#
# Given N, write a function to return the number of knight's tours on an N by N chessboard.

EMPTY = -1

def print_board(board:list):
    for x in range(len(board)):
        for y in range(len(board[0])):
            val = board[x][y]


def is_valid_move(x, y, n, board: list) -> bool:
    return 0 <= x < n and 0 <= y < n and board[x][y] == EMPTY

def knights_tour(n: int, start_x: int = 0, start_y: int = 0) -> int:
    solutions = []  # list of tuple for coordinates
    board = [[EMPTY] * n for _ in range(n)]
    assert len(board) == n and len(board[0]) == n
    pass
