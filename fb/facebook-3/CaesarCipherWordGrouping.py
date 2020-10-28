# Given a caesar cipher and a list of words, determine which words belong to the same group according to the cipher
# for example:
# ['abc', 'bcd', 'bde', 'cfg']
# would be split into two groups
# ['abc', 'bcd'] and ['bde', 'cfg'], since 'abc' and 'bcd' can be shifted from to the other

"""
After understanding what the cipher was doing, basically everything that can be shifted into one another is in the
same group. So this can be reduced to a grouping program, where the key are sequences of diff between characters
in each word. And we have to watch for diff that's two digits, coz they can be confused with two different diff values,
like 'abc' -> '11' and 'al' -> 11, so we need to separate these diffs.

'abc' -> '1,1'
'bcd' -> '1,1'

"""
# GG: the second question from the coding session, I didn't have time to finish coding this up, but I got most of the
#  logics conveyed to the interviewer. One mistake I made, now looking back, is I introduced a base for the first
#  character to diff from. That breaks the grouping of single character strings like 'a' with 'b'
from collections import defaultdict


def cipher_hash(word: str) -> str:
    if not word:
        return '*'
    res = []
    for i in range(1, len(word)):
        res.append(str(ord(word[i]) - ord(word[i - 1])))
    return ",".join(res)


assert cipher_hash('') == '*'
assert cipher_hash('a') == cipher_hash('b') == ''
assert cipher_hash('abc') == '1,1'


def cipher_grouping(lis: list) -> list:
    # This should be O(n) in time and O(n) in space, where n is total len of all words in the list
    assert lis
    lex = defaultdict(list)
    for one_word in lis:
        lex[cipher_hash(one_word)].append(one_word)
    return [values for k, values in lex.items()]


assert cipher_grouping(['abc', 'bcd', 'bde', 'cef']) == [['abc', 'bcd'], ['bde', 'cef']]
assert cipher_grouping(['a', 'b', 'c', '']) == [['a', 'b', 'c'], ['']]
