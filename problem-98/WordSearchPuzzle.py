# This problem was asked by Coursera.
#
# Given a 2D board of characters and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those
# horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# For example, given the following board:
#
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# exists(board, "ABCCED") returns true, exists(board, 'SEE') returns true, exists(board, "ABCB") returns false.


def snake_word_search(board: list, word: str) -> bool:
    # This is dfs looking for the first character match in given word, if found, we dfs explore and find following
    # matches.
    # Assume width of the board is n, height of the board is m, and size of target word is s, then this solution is
    # O(n*m) in time and O(s) in space

    if not board or not word:
        return False

    def find_neighbor_locs(bd: list, row: int, col: int) -> list:
        res = []
        width, height = len(bd[0]), len(bd)
        if row > 0:
            res.append((row - 1, col))
        if col > 0:
            res.append((row, col - 1))
        if row < height - 1:
            res.append((row + 1, col))
        if col < width - 1:
            res.append((row, col + 1))
        return res

    def explore_and_mark(bd: list, target: str, row: int, col: int, visited: set) -> bool:
        if len(target) == 0:
            return True

        neighbor_locs = find_neighbor_locs(bd, row, col)

        for neighbor_r, neighbor_c in neighbor_locs:
            if (neighbor_r, neighbor_c) not in visited and bd[neighbor_r][neighbor_c] == target[0]:
                visited.add((neighbor_r, neighbor_c))
                if explore_and_mark(bd, target[1:], neighbor_r, neighbor_c, visited):
                    return True
        return False

    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == word[0]:
                visited = {(r, c)}
                found = explore_and_mark(board, word[1:], r, c, visited)
                if found:
                    return True
    return False


test_board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

assert not snake_word_search([], 'some')
assert not snake_word_search(test_board, '')
assert snake_word_search(test_board, 'ABCCED')
assert snake_word_search(test_board, 'SEE')
assert not snake_word_search(test_board, 'ABCB')
