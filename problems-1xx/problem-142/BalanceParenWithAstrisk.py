# This problem was asked by Google.
#
# You're given a string consisting solely of (, ), and *. * can represent either a (, ), or an empty string.
# Determine whether the parentheses are balanced.
#
# For example, (()* and (*) are balanced. )*( is not balanced.

"""
This smells like a dynamic programming problem.

let B(i, j) be substring from i index and j index, both INCLUSIVE, and C(i) be the character at index i.
these are the ways to consider a new character at j, and have B(i, j) be true;
1. C(j) is balanced by itself, and B(i, j-1) is already balanced, aka when C(j) is *
2. there's a C(k) where B(i, k) is balanced, and C(k+1, j) is balanced


So this is a dp problem with a 2D memo table and starts with the main diagonal
"""


def is_balanced(a: chr, b: chr) -> bool:
    assert a
    assert b
    if (a == '(' and b == ')') or (a == '(' and b == '*') or (a == '*' and b == ')'):
        return True
    return False


# def is_balanced_with_parens_asterisks(s: str) -> bool:
#     if s == '':
#         return True
#
#     n = len(s)
#     memo = [[False for _ in range(n)] for _ in range(n)]
#     for i in range(n):
#         if s[i] == '*':
#             memo[i][i] = True
#         if i + 1 < n:
#             if is_balanced(s[i], s[i + 1]):
#                 memo[i][i + 1] = True
#
#     for window_size in range(2, n):
#         for r in range(n - window_size):
#             c = r + window_size
#             if memo[r + 1][c - 1] and is_balanced(s[r], s[c]):
#                 memo[r][c] = True
#             else:
#                 for i in range(r, c + 1):
#                     if memo[r][i]:
#                         if (is_balanced(s[i + 1], s[c]) and i + 1 < c and memo[i+1][c-1]) or (is_balanced(s[i+1], s[c])):
#                             memo[r][c] = True
#
#     return memo[0][n - 1]

# GG: I went for dynamic programming solution, but there are more efficient ones. Plus I failed at the dp version
# SEE: https://leetcode.com/problems/valid-parenthesis-string/discuss/?currentPage=1&orderBy=most_votes&query=
def is_balanced_with_parens_asterisks(s: str) -> bool:
    # assert len(s) > 0
    max_valid_open, min_valid_close = 0, 0
    for c in s:
        if c == '(':
            max_valid_open += 1
            min_valid_close += 1
        elif c == ')':
            max_valid_open -= 1
            min_valid_close -= 1
        else:
            # c == '*'
            max_valid_open += 1
            min_valid_close -= 1
        if max_valid_open < 0:
            return False
        min_valid_close = max(min_valid_close, 0)
    return min_valid_close == 0


assert is_balanced_with_parens_asterisks("")
assert is_balanced_with_parens_asterisks("*")
assert is_balanced_with_parens_asterisks("()")
assert is_balanced_with_parens_asterisks("(*")
assert is_balanced_with_parens_asterisks('*)')
assert is_balanced_with_parens_asterisks('()*')
assert is_balanced_with_parens_asterisks('*()')
assert is_balanced_with_parens_asterisks('(()*')
assert not is_balanced_with_parens_asterisks('())')
assert not is_balanced_with_parens_asterisks(')*')
assert not is_balanced_with_parens_asterisks('*(')
assert not is_balanced_with_parens_asterisks(')(')
assert not is_balanced_with_parens_asterisks('(()(')
assert is_balanced_with_parens_asterisks('()()')
assert not is_balanced_with_parens_asterisks('()(()')
assert is_balanced_with_parens_asterisks('()(*()')
assert not is_balanced_with_parens_asterisks('()(*(()')
assert is_balanced_with_parens_asterisks('(())()')
assert is_balanced_with_parens_asterisks('(()*)()')
assert is_balanced_with_parens_asterisks('(())*()')
assert is_balanced_with_parens_asterisks('()(()*')
assert is_balanced_with_parens_asterisks('()((*)')


