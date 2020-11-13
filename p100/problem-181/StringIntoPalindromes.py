# This problem was asked by Google.
#
# Given a string, split it into as few strings as possible such that each string is a palindrome.
#
# For example, given the input string racecarannakayak, return ["racecar", "anna", "kayak"].
#
# Given the input string abc, return ["a", "b", "c"].

#GOOGLE
#DP
#DPMatrixMul
#PalindromePartitioning

# GG: This took a lot of effort for even the naive solution, and I don't have the back tracking done yet.
"""
Not sure where to start at first. This smells like a dynamic programming problem though

As few as possible, aka, each of the palindrome should be as big as possible.

Given a string, worst case is it will be split up to n palindromes, where each is one character long.

After half an hour of doodling, I think we need two 2D array.
p(i, j) is True if substring i..j is a palindrome
c(i, j) is how many minimum palindrome needed to cover this substring

p(i, j) = {
    True if i = j and p(i +1, j-1) is True
    False otherwise
}

Then
c(i, j) = {
    1 if p(i, j) is True
    min( c(i, m) + c(m+i, j)) where i < m < j
}

This would get me the minimum num of palindrome needed, but I guess I have to back trace, or modify the code to find the
individual palindromes
"""

def string_to_fewest_palindromes(s: str) -> list:
    assert s
    n = len(s)
    # p = [[False for _ in range(n)] for _ in range(n)]
    # for i in range(n):
    #     p[i][i] = True

    # # first dp memo table for whether a substring is a palindrome
    # for window in range(1, n):
    #     # window will point at an inclusive end of the substring
    #     for i in range(n):
    #         if i + window < n:
    #             sub_str = s[i: i + window + 1]
    #             if sub_str[-1] == sub_str[0]:
    #                 p[i][i + window] = True if window == 1 or p[i+1][i+window-1] else False

    # second dp memo for how many palindrome is needed to cover this substring
    c = [[1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        c[i][i] = 1

    # # c[0][n-1] would give us the min number of palindrome to cover the whole string
    # for window in range(1, n):
    #     for i in range(n):
    #         if i + window < n:
    #             if p[i][i+window]:
    #                 c[i][i+window] = 1
    #             else:
    #                 c[i][i+window] = min([c[i][i+m] + c[i+m+1][i+window] for m in range(window)])

    # break ups that form the substring from i to j
    b = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        b[i][i].append(s[i])

    for window in range(1, n):
        for i in range(n):
            if i + window < n:
                sub_str = s[i: i + window + 1]
                if sub_str[-1] == sub_str[0] and (window == 1 or c[i+1][i+window-1] == 1):
                    c[i][i+window] = 1
                    # b[i][i+window] = [s[i:i+window+1]]
                else:
                    c[i][i+window] = min([c[i][i+m] + c[i+m+1][i+window] for m in range(window)])

    return []


print(string_to_fewest_palindromes('abac'))