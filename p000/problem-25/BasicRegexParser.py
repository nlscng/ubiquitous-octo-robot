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
    if text == pattern == '':
        return True
    elif text == '':
        return False
    elif pattern == '':
        return False

    text = ' ' + text
    pattern = ' ' + pattern
    lt = len(text)
    lp = len(pattern)
    memo = [[False] * lp for _ in range(lt)]
    memo[0][0] = True  # empty text and empty pattern is a match

    # special case, handle the first row, where we have empty txt, but non-empty pattern; this row isn't always false
    for i in range(1, lp):
        memo[0][i] = True if pattern[i] == '.' or pattern[i] == '*' else False

    for i in range(1, lt):
        # watch for the added col/row of 0th, we deal with i, j in memo, but i-1, j-1 in text and pattern
        for j in range(1, lp):
            if text[i] == pattern[j] or pattern[j] == '.':
                # if i text match char pattern at j, or j is wildcard, the this result is based on last char txt and
                # last char pattern match
                memo[i][j] = memo[i - 1][j - 1]
            elif pattern[j] == '*':
                if text[i] == pattern[j - 1] or pattern[j - 1] == '.':
                    # if pattern char is star, and we can fold this txt chr to prev one, aka last txt char
                    # is the same, or is a wild card, then this result is result of last txt char matching with
                    # current pattern chr
                    memo[i][j] = memo[i - 1][j]
                else:
                    # else, we can't fold this txt chr into the *, so we look for the zero count match for *
                    # which is, zero count for the pattern char right before this j,
                    # so the result is if text up to i is a regex match up to pattern - 2
                    zero_occurrence_result = memo[i][j - 2] if j > 1 else False
                    memo[i][j] = zero_occurrence_result
            else:
                memo[i][j] = False

    return memo[lt - 1][lp - 1]


assert is_match("", "")
assert is_match("a", "a")
assert is_match("abc", "abc")

assert not is_match('a', '')
assert not is_match('', 'a')
assert not is_match('a', 'b')
assert not is_match('abc', 'cab')

assert is_match("abc", "a.c")
assert is_match("abc", "a..")
assert is_match("abc", "a..*")

assert not is_match('a', 'a.')
assert not is_match('ab', 'ab.')
assert not is_match('ac', 'a.c')
assert not is_match('acb', 'a.c')

assert is_match("a", "a*")
assert is_match("aa", "a*")
assert is_match("aaa", "a*")

assert not is_match("ab", "a*")
assert not is_match("aab", "a*")

assert is_match("abb", "a.*")
assert is_match("abbcd", 'a.*d')
assert is_match("abbcd", 'ab*.d')
assert is_match("aa", 'a*.')
assert is_match('xaabyc', 'xa*b.c')
