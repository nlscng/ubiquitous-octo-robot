# This problem was asked by Google.
#
# Given a word W and a string S, find all starting indices in S which are anagrams of W.
#
# For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.


'''

This feels like a sliding window counting problem. First get the count of the letters in target word, keep that in
a dict, and scan through the string with a window size of n, n is number of letters in word, and when they match,
record the starting index.

 abxaba
  l
   r

a:1, b:1
'''

from collections import defaultdict


def have_same_counts(a: {}, b: {}) -> bool:
    if not a or not b:  # since I am using defaultdict, the size of the dict may not be the same while having same
        # meaningful count, so a length check here is erroneous
        return False

    for k, v in a.items():
        if v != 0 and b[k] != v:
            return False
    return True


def find_anagram(w: str, s: str) -> []:
    # this is O(
    if not w or not s:
        return []

    len_w = len(w)
    len_s = len(s)
    target_count = defaultdict(int)
    for one_letter in w:
        target_count[one_letter] += 1

    moving_count = defaultdict(int)
    l_ptr, r_ptr = 0, len_w
    for one_letter in s[l_ptr: r_ptr]:
        moving_count[one_letter] += 1

    res = []
    while r_ptr <= len_s:  # since i am using r_ptr as exclusive boundary
        if have_same_counts(moving_count, target_count):
            res.append(l_ptr)

        # update moving count
        if r_ptr < len_s:
            moving_count[s[l_ptr]] -= 1
            moving_count[s[r_ptr]] += 1
        l_ptr += 1
        r_ptr += 1

    return res


assert not find_anagram('', '')
assert find_anagram('ab', 'abxaba') == [0, 3, 4], "Actual: {}".format(find_anagram('ab', 'abxaba'))

