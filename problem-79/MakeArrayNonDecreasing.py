# This problem was asked by Facebook.
#
# Given an array of integers, write a function to determine whether the array could become non-decreasing by
# modifying at most 1 element.
#
# For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the
# array non-decreasing.
#
# Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing
# array.


def make_non_decreasing(arr: list) -> bool:
    if not arr:
        return False
    if len(arr) == 1:
        return True

    has_one_fault = False
    for idx, val in enumerate(arr):
        if idx == 0:
            continue
        if arr[idx - 1] > arr[idx]:
            if has_one_fault:
                return False
            has_one_fault = True

    return True


assert make_non_decreasing([10, 5, 7])
assert not make_non_decreasing([10, 5, 1])
