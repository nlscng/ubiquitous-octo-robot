# This problem was asked by Google.
#
# Given a string which we can delete at most k, return whether you can make a palindrome.
#
# For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'.
#

"""
waterrfetawx
      *    *
waterretaw


This feels like a DP problem.

Create a 2D memo table, both axis are

"""

# GG: took me a day to think about this, I was only certain this is a dp

def delete_k_palindrome(s: str, k: int) -> bool:
    assert k >= 0
    if len(s) < 2:
        return True

    n = len(s)
    # create a 2D table that holds in each (i, j) how many deletion is needed to make a palindrome
    # i, j are indices into the string, s.t i < j, i >=0, j >= 0
    # so our answer will sit at upper right corner

    # let p(i, j) be number of deletion to make s_i ... s_j a palindrome
    # then p(i, j) =
    # if s_i == s_j, p(i + 1, j - 1)
    # else, 1 + min( p(1, j - 1), p(i + 1, j)), aka adding one deletion by either dropping the left most or right most
    memo = [[0 for _ in range(n)] for _ in range(n)]

    # all single char substring is a palindrome
    for i in range(n):
        memo[i][i] = 0
        if i + 1 < n:
            # GG: this is important, palindrome can have a single char center, or two mirrored strings
            memo[i][i+1] = 0 if s[i] == s[i+1] else 1

    for window in range(2, n):
        for i in range(n - window):
            j = i + window
            if s[i] == s[j]:
                memo[i][j] = memo[i+1][j-1]
            else:
                drop_i = memo[i+1][j]
                drop_j = memo[i][j-1]
                memo[i][j] = 1 + min(drop_i, drop_j)

    return memo[0][n-1] <= k


assert delete_k_palindrome("a", 0)
assert delete_k_palindrome("aaa", 2)
assert not delete_k_palindrome("add", 0)
assert delete_k_palindrome("waterrfetawx", 2)
assert not delete_k_palindrome("waterrfetawx", 1)
assert delete_k_palindrome("waterrfetawx", 3)
assert delete_k_palindrome("malayalam", 0)
assert delete_k_palindrome("malayalam", 1)
assert delete_k_palindrome("asdf", 5)
assert not delete_k_palindrome("asdf", 2)
