"""
Binary search has always been, well binary search, to me, looking for one element in a sorted environment.

But I've come across where binary search can be used to, instead of looking for a specific target, find ranges,
unequal relations. So I am going to practice writing one binary search for that.

Given an array of sorted int, and a value k, find number of elements that are in this array that are smaller than k.
The value k is not necessary in the array.
"""

##

from typing import List


def binary_search_smaller(lis: List[int], k: int) -> int:
    # GG: I guess in thinking though binary search, try not to worry about inclusivity on indices.
    assert lis
    low, high = 0, len(lis) - 1
    mid = (high + low) // 2

    # sanity check, k might be too small or too large anyway, and this saves me from handling corner cases later
    if k < lis[0]:
        return 0
    if k > lis[-1]:
        return len(lis)

    # I am looking for mid, the index of the element which is the smallest that's not smaller than k
    while low < high:
        if lis[mid] < k:
            low = mid + 1
            mid = (high + low) // 2
        else:
            high = mid
            mid = (high + low) // 2

    return mid


assert binary_search_smaller([2, 4, 6, 8, 10], 7) == 3
assert binary_search_smaller([2, 4, 6, 8, 10], 6) == 2
assert binary_search_smaller([1, 2, 3], 1) == 0
assert binary_search_smaller([1, 2, 3], 4) == 3
assert binary_search_smaller([1, 2, 3], -1) == 0
