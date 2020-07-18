# This problem was asked by Square.
#
# Given a string and a set of characters, return the shortest substring containing all the characters in the set.
#
# For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".
#
# If there is no substring containing all the characters in the set, return null.


'''
figehaeci, {a, e, i} => 'aeci'

sliding window, keep a count in a dict, record possible solution when count of all character in set is 1,
the window moves right edge if target chars are not met (aka not all count of them are 1), the window moves the
left edge if all count are 1 and greater


figehaeci, {a, e, i} => 'aeci'
      l
         r

a: 1
e: 1
i: 1

abcd, b
 l
  r

b: 1
cur_shorted = 'ab'
'''


def update_has_all(count: {}) -> bool:
    for one_key in count:
        if count[one_key] < 1:
            return False
    return True


def shortest_substring(word: str, targets: set) -> str:
    if not word or not targets:
        return None

    l_walker = r_walker = 0
    count = {x: 0 for x in targets}
    n = len(word)
    cur_shortest = None
    has_all = False

    while (not has_all and r_walker < n) or (has_all and l_walker < r_walker):  # GG: tricky to get right
        if not has_all:
            c = word[r_walker]
            if c in targets:
                count[c] += 1
                has_all = update_has_all(count)
            r_walker += 1
        else:
            sub = word[l_walker: r_walker]
            if cur_shortest is None or len(cur_shortest) > len(sub):
                cur_shortest = sub

            c = word[l_walker]
            if c in targets:
                count[c] -= 1
                has_all = update_has_all(count)
            l_walker += 1

    return cur_shortest


assert shortest_substring('', {'a', 'b'}) is None, "Actual: {}".format(shortest_substring('', {'a', 'b'}))
assert shortest_substring('abcd', {'a'}) == 'a'
assert shortest_substring('abcd', {'d'}) == 'd'
assert shortest_substring('abcdebde', {'b', 'd'}) == 'bd'
assert shortest_substring('figehaeci', {'a', 'e', 'i'}) == 'aeci'
