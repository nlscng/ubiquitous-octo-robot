# This problem was asked by Microsoft.
#
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#
# For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4]. Return its
# length: 4.
#
# Your algorithm should run in O(n) complexity.


'''

100, 4, 200, 1, 3, 2

copy them to set for easier look up

spin through the list. given an element, ask if the next or prev element is in set.
if yes, create a buffer for this consecutive seq, then continue with the two boundaries
if not, record the current max len of the buffer, start over with next element

seen: 100,
seq: 4
cur_max:

'''


def longest_sequence(arr: list) -> int:
    # this is O(n) in time, since all member are seen one time
    # this is O(n) in space too, although there's a set and a list that's linear to n, so it's like O(2n)
    # GG: interesting problem
    if not arr:
        return 0
    if len(arr) == 1:
        return 1

    members = set(arr)
    seen = set()
    cur_max_len = 0

    for a in arr:
        if a not in seen:
            seen.add(a)
            seq = [a]
            prev, next = a - 1, a + 1
            while prev in members or next in members:
                if prev in members:
                    seq = [prev] + seq
                    seen.add(prev)
                    prev -= 1
                else:
                    seq.append(next)
                    seen.add(next)
                    next += 1
            cur_max_len = max(cur_max_len, len(seq))

    return cur_max_len


assert longest_sequence([]) == 0
assert longest_sequence([3]) == 1
assert longest_sequence([100, 4, 200, 1, 3, 2]) == 4
