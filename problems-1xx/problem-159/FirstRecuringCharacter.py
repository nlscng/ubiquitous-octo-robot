# This problem was asked by Google.
#
# Given a string, return the first recurring character in it, or null if there is no recurring character.
#
# For example, given the string "acbbac", return "b". Given the string "abcdef", return null.

"""
First idea is turning this into a counting problem, then first character to exceed count of 1 is the answer.

Slight optimization is, since I care about count of one, I can use a set for tracking things, and if a newly scanned
character is already in set, then I've found it.

Both options are of time complexity O(n), and space of O(n)
"""


def first_recurring(word: str) -> chr:
    assert word and word.split() == [word]

    seen = set()
    for c in word:
        if c not in seen:
            seen.add(c)
        else:
            return c
    return None


assert first_recurring("acbbac") == 'b'
assert first_recurring('abcdef') is None
