# This problem was asked by Airbnb.

# Given a list of words, find all pairs of unique indices such that the concatenation of the two words is a palindrome.

# For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)].

"""
The naive approach is easy to see, but I am not seeing a better solution yet. Naive brute force would take O(n^2*k) in time.


After researching/googling, a better idea is to check if word A's prefix mirrors any word B, then confirm word A's
suffix is itself a palindrome.

Start by inventory the list of words for easy lookup (with a dict), then spin through them one by one. Take one word, check if any paritial (or full) of it, reversed, is found in another place in the dict.
"""


def is_palindrome(w: str) -> bool:
    return w == w[::-1]


assert is_palindrome('')
assert is_palindrome(' ')
assert is_palindrome('a')

"""
code, edoc

lex: {
    code: 0
    edoc: 1
}
word: code
idx: 0
i: 0 / 4
pre=
suff=code
mirror=edoc
"""


def pair_palindrome(words: list) -> list:
    res = []
    if not words:
        return res

    lex = dict()
    for idx, word in enumerate(words):
        lex[word] = idx

    for idx, word in enumerate(words):
        # no cutting up words, yet
        if word[::-1] in lex and lex[word[::-1]] != idx:
            res.append([idx, lex[word[::-1]]])

        # divvy up words, two cases, be sure to skip whole word check since it's done
        for i in range(1, len(word)):
            pre = word[:i]
            suff = word[i:]
            mirror = pre[::-1]
            if mirror in lex and lex[mirror] != idx and is_palindrome(suff):
                res.append([idx, lex[mirror]])
            mirror = suff[::-1]
            if mirror in lex and lex[mirror] != idx and is_palindrome(pre):
                res.append([lex[mirror], idx])
    return res


print(pair_palindrome(['code', 'edoc']))
print(pair_palindrome(['da', 'd']))
print(pair_palindrome(["abc", "xyxcba", "geekst", "or", "keeg", "bc"]))

assert pair_palindrome(['code', 'edoc', 'da', 'd']) == [[0, 1], [1, 0], [2, 3]]
assert pair_palindrome(["abc", "xyxcba", "geekst", "or", "keeg", "bc"]) == [[0, 1]]
