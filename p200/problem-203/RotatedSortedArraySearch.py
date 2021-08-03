# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. Find the minimum
# element in O(log N) time. You may assume the array does not contain duplicates.
#
# For example, given [5, 7, 10, 3, 4], return 3.

from typing import Optional


def rotated_sorted_array_search(arr: list) -> Optional[int]:
    assert len(arr) > 0

    b, e = 0, len(arr) - 1  ## e needs to be inclusive

    while b < e:
        if abs(b - e) == 1:
            return min(arr[b], arr[e])

        m = (b + e) // 2
        if arr[b] < arr[e]:
            return arr[b]
        elif arr[b] > arr[m]:
            e = m
        else:
            b = m + 1

    return arr[b]


assert rotated_sorted_array_search([1, 2, 3]) == 1
assert rotated_sorted_array_search([1]) == 1
assert rotated_sorted_array_search([3, 1, 2]) == 1
assert rotated_sorted_array_search([3, 4, 1, 2]) == 1
assert rotated_sorted_array_search([4,5,6,2,3]) == 2
