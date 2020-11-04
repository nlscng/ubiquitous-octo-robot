# This problem was asked by Dropbox.
#
# Given a string s and a list of words words, where each word is the same length, find all starting indices of
# substrings in s that is a concatenation of every word in words exactly once.
#
# For example, given s = "dogcatcatcodecatdog" and words = ["cat", "dog"], return [0, 13], since "dogcat" starts at
# index 0 and "catdog" starts at index 13.
#
# Given s = "barfoobazbitbyte" and words = ["dog", "cat"], return [] since there are no substrings composed of "dog"
# and "cat" in s.
#
# The order of the indices does not matter.


# GG: not sure where to start
"""
There's a linear time substring search algorithm, KMP or something. Assuming that's optimized to something like linear
time, then I can build a list of substring to search for, which are permutations of the words put together, and scan
the string for them.


"""


def permutation(lis: list) -> list:
    assert lis
    res = []
    n = len(lis)

    def recur(built: list, remain: list):
        if len(built) == n:
            res.append("".join(built))
        else:
            for i in range(len(remain)):
                recur(built + [remain[i]], remain[:i] + remain[i + 1:])

    recur([], lis)
    return res


def substring_words_search(s: str, words: list) -> list:
    # GG: the permutation is O(n!) in time, and the search of permuted-words should be O(m), where n is num of words
    #  to combine and search for, m is lenngth of s to search from the last assertion is goofy, and needs cleaning up
    assert s and words and len(words[0]) == len(words[-1])

    res = []
    target_words = permutation(words)
    for one_word in target_words:
        if one_word in target_words:
            res.append(s.find(one_word))

    return sorted(res)


assert substring_words_search('dogcatcatcodecatdog', ['cat', 'dog']) == [0, 13]
assert substring_words_search('barfoobazbitbyte', ['cat', 'dog']) == []
