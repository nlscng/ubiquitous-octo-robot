# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# The edit distance between two strings refers to the minimum number of character insertions, deletions,
# and substitutions required to change one string to the other. For example, the edit distance between “kitten” and
# “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.
#
# Given two strings, compute the edit distance between them.

def edit_distance(a: str, b: str):
    if not isinstance(a, str) or not isinstance(b, str):
        return None
    if not a:
        return len(b)
    elif not b:
        return len(a)

    # let D(i, j) be the edit distance for word_a and word_b, notice we treat first letter in a word with index 1
    # so row and column 0 in memo are not pointing at actual letter in words
    memo = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

    # init memo for base cases, where either a is empty or b is empty
    for i in range(len(memo)):
        memo[i][0] = i  # word b is empty, so distance is just how long a is
    for j in range(len(memo[0])):
        memo[0][j] = j  # word a is empty, so distance is just how long b is

    for i in range(1, len(memo)):
        for j in range(1, len(memo[0])):
            if a[i - 1] == b[j - 1]:            # be careful indexing into words, we are using
                memo[i][j] = memo[i - 1][j - 1]
            else:
                memo[i][j] = min(
                    memo[i - 1][j] + 1,         # delete to make a_i to match b_j
                    memo[i - 1][j - 1] + 1,     # replace a_i to match b_j
                    memo[i][j - 1] + 1          # insert a_i to match b_j
                )
    return memo[-1][-1]


assert edit_distance("", "") == 0
assert edit_distance("a", "b") == 1
assert edit_distance("abc", "") == 3
assert edit_distance("abc", "abc") == 0
assert edit_distance("kitten", "sitting") == 3
