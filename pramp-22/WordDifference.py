# Given two strings of uppercase letters source and target, list (in string form) a sequence of edits to convert from
# source to target that uses the least edits possible.
#
# For example, with strings source = "ABCDEFG", and target = "ABDFFGH" we might return: ["A", "B", "-C", "D", "-E",
# "F", "+F", "G", "+H"
#
# More formally, for each character C in source, we will either write the token C, which does not count as an edit;
# or write the token -C, which counts as an edit.
#
# Additionally, between any token that we write, we may write +D where D is any letter, which counts as an edit.
#
# At the end, when reading the tokens from left to right, and not including tokens prefixed with a minus-sign,
# the letters should spell out target (when ignoring plus-signs.)
#
# In the example, the answer of A B -C D -E F +F G +H has total number of edits 4 (the minimum possible),
# and ignoring subtraction-tokens, spells out A, B, D, F, +F, G, +H which represents the string target.
#
# If there are multiple answers, use the answer that favors removing from the source first.
import copy


def diffBetweenTwoStrings(src, tgt):
    # TBC: finish out the dynamic programming solution
    """
    @param source: str
    @param target: str
    @return: str[]
    :param src:
    :param tgt:
    :return:
    """
    ss = len(src) + 1
    ts = len(tgt) + 1

    memo = [[list() for i in range(ts)] for j in range(ss)]
    assert len(memo) == ss
    assert len(memo[0]) == ts

    for i in range(1, ts):
        last = copy.deepcopy(memo[0][i-1])
        last.append('+' + tgt[i-1])
        memo[0][i] = last

    for i in range(1, ss):
        last = copy.deepcopy(memo[i-1][0])
        last.append('-' + src[i-1])
        memo[i][0] = last

    print(memo)

    pass


diffBetweenTwoStrings('a', 'ab')
