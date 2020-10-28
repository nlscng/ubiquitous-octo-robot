# This problem was asked by Amazon.
#
# Given a string, determine whether any permutation of it is a palindrome.
#
# For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome. daily
# should return false, since there's no rearrangement that can form a palindrome.

"""
Checking if a word is a permutation of palindrome is essentially checking the count of each characters, and see
if they can make up a count for a palindrome.

A palindrome would have all characters count to be even, except maybe one of them to be odd.
"""

from collections import defaultdict


def get_counts(word: str) -> dict:
    assert word
    count = defaultdict(int)

    for c in word:
        count[c] += 1
    return count


def is_permu_palindrome(word: str) -> bool:
    assert word.split()[0] == word
    count = get_counts(word)
    num_odd = 0
    for v in count.values():
        if v % 2 != 0:
            num_odd += 1
    return num_odd <= 1


assert is_permu_palindrome("carrace")
assert not is_permu_palindrome("daily")
