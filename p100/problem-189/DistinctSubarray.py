# This problem was asked by Google.
#
# Given an array of elements, return the length of the longest subarray where all its elements are distinct.
#
# For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray of distinct elements is [5,
# 2, 3, 4, 1].

"""
This should be a two pointers problem. I can have a slow walker and a fast walker, and by maintaining a set of distinct
elements. I move the fast pointer forward as long it's not in the set, I move the left pointer if the right is in the
set, and the left pointer has to be moved until the right point value is found and removed from the set, then we start
over til right pointer reaches the end


  5, 1, 3, 5, 2, 3, 4, 1
  s
           f
{5, 1, 3
"""

from typing import List


def longest_distinct_subarray(lis: List[int]) -> int:
    assert lis
    cur = set()
    max_len = 0
    slow, fast = 0, 0

    while fast < len(lis):
        if lis[fast] not in cur:
            cur.add(lis[fast])
            fast += 1
            max_len = max(max_len, len(cur))
        else:
            while lis[slow] != lis[fast]:
                # search for value that has a dupe collison
                cur.remove(lis[slow])
                slow += 1

            # GG: this last step is important
            cur.remove(lis[slow])
            slow += 1

    return max_len


assert longest_distinct_subarray([5, 1, 3, 5, 2, 4, 1]) == 5
assert longest_distinct_subarray([8, 3, 0, 5, 4, 2, 6, 3, 0, 7, 4]) == 7
