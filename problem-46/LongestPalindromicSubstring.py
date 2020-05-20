# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum
# length, return any one.
#
# For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of
# "bananas" is "anana".


def longest_palindromic_substring(s: str) -> str:
    # build a memo table, where row r is r-th index into the string, and col c is c-th index into the string, and
    # substring s[c:r+1] is the substring being noted in this memo[r, c]

    row = col = len(s)
    memo = [[False] * col for _ in range(row)]

    # init all single letter substring to True, ie a palindrome
    # and all two chars long substring to be True, if it's a palindrome
    for i in range(row):
        memo[i][i] = True
        if i + 1 < row and s[i] == s[i + 1]:
            memo[i][i + 1] = True

    # let p(i, j) denote if substring of s[j:i+1] is a palindrome, i >= j
    # I define the table this way so I will only look at upper right half of it for memo
    # then p(i, j):
    # True if s[i] == s[j] and p(i-1, j+1) is true

    cur_longest_palindrome = ''

    # GG: fill the memo table from the diagonal to rest, and with a sliding window that grows in size
    for window in range(2, col):
        for i in range(row - window):
            r, c = i, i + window
            if memo[r + 1][c - 1] and s[r] == s[c]:
                memo[r][c] = True
                if c - r > len(cur_longest_palindrome):
                    cur_longest_palindrome = s[r:c+1]

    return cur_longest_palindrome


assert longest_palindromic_substring('') == ''
assert longest_palindromic_substring('a') == 'a'
assert longest_palindromic_substring('ab') == ''
assert longest_palindromic_substring('aabcdcb') == 'bcdcb'
assert longest_palindromic_substring('bananas') == 'anana'
