# Basic Regex Parser Implement a regular expression function isMatch that supports the '.' and '*' symbols. The
# function receives two strings - text and pattern - and should return true if the text matches the pattern as a
# regular expression. For simplicity, assume that the actual symbols '.' and '*' do not appear in the text string and
# are used as special symbols only in the pattern string.
#
# In case you aren’t familiar with regular expressions, the function determines if the text and pattern are the
# equal, where the '.' is treated as a single a character wildcard (see third example), and '*' is matched for a zero
#  or more sequence of the previous letter (see fourth and fifth examples). For more information on regular
#   expression matching, see the Regular Expression Wikipedia page.
#
# Explain your algorithm, and analyze its time and space complexities.
#
# Examples:
#
# input:  text = "aa", pattern = "a"
# output: false
#
# input:  text = "aa", pattern = "aa"
# output: true
#
# input:  text = "abc", pattern = "a.c"
# output: true
#
# input:  text = "abbb", pattern = "ab*"
# output: true
#
# input:  text = "acd", pattern = "ab*c."
# output: true

# SEE: https://leetcode.com/problems/regular-expression-matching/solution/
# SEE: https://www.youtube.com/watch?v=l3hda49XcDE&feature=emb_logo
# GG: a tricky but worthy dynamic programming problem
def is_match(text, pattern):
    memo = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
    memo[0][0] = True  # empty text and empty pattern is a match
    lt = len(text)
    lp = len(pattern)

    for i in range(1, lt + 1):
        # watch for the added col/row of 0th, we deal with i, j in memo, but i-1, j-1 in text and pattern
        for j in range(1, lp + 1):
            if text[i - 1] == pattern[j - 1] or pattern[j - 1] == '.':
                # if i text match char pattern at j, or j is wildcard
                memo[i][j] = memo[i - 1][j - 1]
            elif pattern[j - 1] == '*':
                zero_occurrence_result = memo[i][j - 2]
                # the case where pattern is a*, and we consider * to match 0 occurrence, this is always be possible
                memo[i][j] = memo[i - 1][j] or zero_occurrence_result if text[i - 1] == pattern[j - 2] or pattern[
                    j - 2] == '.' else zero_occurrence_result
                # if the pattern before the * is a char that and we match, or that char is the wildcard, we take the
                # pattern match result of the same pattern (j), but drop our current txt at (i)
            else:
                memo[i][j] = False

    return memo[lt][lp]


assert is_match("", "")
assert is_match("a", "a")
assert is_match("abc", "abc")
assert is_match("abc", "a.c")
assert is_match("abb", "a.*")
assert is_match("abbcd", 'a.*d')
assert is_match("abbcd", 'ab*.d')
