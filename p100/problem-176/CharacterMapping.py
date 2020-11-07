# This problem was asked by Bloomberg.
#
# Determine whether there exists a one-to-one character mapping from one string s1 to another s2.
#
# For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.
#
# Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.

"""
This might be actually just comparing number of unique characters in both strings, as functional mappings is a -> b,
and it's ok if domain of A is >= domain of B
"""

def is_mappable(a: str, b: str):
    # this is naive approach, there are ways to do this with smaller complexity,
    assert a and b

    count_a = len(set([c for c in a]))
    count_b = len(set([c for c in b]))

    return count_a >= count_b


assert is_mappable('abc', 'bcd')
assert not is_mappable('foo', 'bar')

