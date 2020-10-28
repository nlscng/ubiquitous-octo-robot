# Find an efficient algorithm to find the smallest distance (measured in number of words) between any two given words
# in a string.
#
# For example, given words "hello", and "world" and a text content of "dog cat hello cat dog dog hello cat world",
# return 1 because there's only one word "cat" in between the two words.

"""
dog cat hello cat dog dog hello cat world

Naive and brute force would be, given the two words a and b, find an instance of a, spin through and find smallest
distance for any b, then try the next a and spin through, compare the smallest found with any instance of a, return
the smallest of the smallest. This should be O(n ^ 2) in time

Another possible improvement is this, build an index using a dictionary, records all the indices of a and b. Say it's
like this:
{
    a: [0, 3, 8]
    b: [6, 12]
}
Then walk through this two lists with two pointers, finding the smallest diff between any number.
"""

from collections import defaultdict
from sys import maxsize


def num_words_between_words(words: str, a: str, b: str) -> int:
    # this should be O(n) in time and O(n) in space
    assert words and a and b
    assert a in words and b in words

    tokenized = words.split()
    pre = defaultdict(list)

    for idx, w in enumerate(tokenized):
        if w == a:
            pre[a].append(idx)
        elif w == b:
            pre[b].append(idx)

    ax = pre[a]
    bx = pre[b]

    aw, bw = 0, 0  # walkers
    min_delta = maxsize

    while aw < len(ax) and bw < len(bx):
        min_delta = min(abs(ax[aw] - bx[bw]), min_delta)
        if ax[aw] < bx[bw]:
            aw += 1
        else:
            bw += 1
    return min_delta - 1


word_bank_1 = "dog cat hello cat dog dog hello cat world"
assert num_words_between_words(word_bank_1, "hello", "world") == 1
assert num_words_between_words(word_bank_1, "hello", "dog") == 0
assert num_words_between_words(word_bank_1, "world", "dog") == 2


def num_words_diff(words: str, a: str, b: str) -> int:
    # GG: the two pointers, idea from google net search
    assert words and a and b
    assert a in words and b in words
    pre = words.split()

    aw, bw = None, None
    min_delta = maxsize
    for idx, w in enumerate(pre):
        if w == a or w == b:
            if w == a:
                aw = idx
            if w == b:
                bw = idx
            if aw and bw:
                min_delta = min(min_delta, abs(aw - bw))
    return min_delta - 1


assert num_words_diff(word_bank_1, "hello", "world") == 1
assert num_words_diff(word_bank_1, "hello", "dog") == 0
assert num_words_diff(word_bank_1, "world", "dog") == 2
