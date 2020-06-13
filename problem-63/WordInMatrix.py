# This problem was asked by Microsoft.
#
# Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in
# the matrix by going left-to-right, or up-to-down.
#
# For example, given the following matrix:
#
# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]
#
#  and the target word
# 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS',
# you should return true, since it's the last row.

def find_word(matrix: list, word: str) -> bool:
    if not matrix or not word:
        return False

    num_row = len(matrix)
    num_col = len(matrix[0])
    word_len = len(word)
    for i in range(num_row):
        for j in range(num_col):
            if (i + word_len <= num_row or j + word_len <= num_col) and matrix[i][j] == word[0]:
                # test horizontal:
                if i + word_len <= num_row and word == "".join([matrix[x][j] for x in range(i, i+word_len)]):
                    return True
                # test vertical
                if j + word_len <= num_col and "".join(matrix[i][j:j+word_len]) == word:
                    return True
    return False


test = [['F', 'A', 'C', 'I'],
        ['O', 'B', 'Q', 'P'],
        ['A', 'N', 'O', 'B'],
        ['M', 'A', 'S', 'S']]

assert find_word(test, "FOAM")
assert find_word(test, "MASS")