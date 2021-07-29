# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. Find the minimum
# element in O(log N) time. You may assume the array does not contain duplicates.
#
# For example, given [5, 7, 10, 3, 4], return 3.

from typing import Optional


def rotated_sorted_array_search(array: list) -> Optional[int]:
    assert len(array) > 0

    b, e = 0, len(array) - 1  ## e needs to be inclusive

    while b < e:
        if array[b] > array[e] and e - b == 1:
            return e

        m = (b + e) // 2
        if array[b] < array[m] < array[e]:
            return array[b]
        elif array[b] > array[m]:
            e = m
        else:
            b = m + 1

    return array[b]


assert rotated_sorted_array_search([1, 2, 3]) == 1
assert rotated_sorted_array_search([1]) == 1
assert rotated_sorted_array_search([3, 1, 2]) == 1
assert rotated_sorted_array_search([3, 4, 1, 2]) == 1
