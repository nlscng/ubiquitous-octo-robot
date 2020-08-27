# Getting a Different Number
# Given an array arr of unique nonnegative integers, implement a function getDifferentNumber that finds the smallest nonnegative integer that is NOT in the array.
#
# Even if your programming language of choice doesn’t have that restriction (like Python), assume that the maximum
# value an integer can have is MAX_INT = 2^31-1. So, for instance, the operation MAX_INT + 1 would be undefined in
# our case.
#
# Your algorithm should be efficient, both from a time and a space complexity perspectives.
#
# Solve first for the case when you’re NOT allowed to modify the input arr. If successful and still have time,
# see if you can come up with an algorithm with an improved space complexity when modifying arr is allowed. Do so
#  without trading off the time complexity.
#
# Analyze the time and space complexities of your algorithm.
#
#
# input:  arr = [0, 1, 2, 3]
#
# output: 4


def get_different_number(arr):
    # this is O(n) in time and O(n) in space
    # without modifying input
    n = len(arr)
    flags = [False] * n

    # flags of if the expected num is present in array
    for i in arr:
        if 0 <= i < n:
            flags[i] = True

    # find first missing non-neg num
    for idx in range(n):
        if not flags[idx]:
            return idx

    return n


assert get_different_number([0]) == 1
assert get_different_number([0, 1, 2]) == 3
assert get_different_number([1, 3, 0, 2]) == 4
assert get_different_number([100000]) == 0
assert get_different_number([1, 0, 3, 4, 5]) == 2
assert get_different_number([0, 999999]) == 1
assert get_different_number([0, 1, 4, 2, 5, 6, 3]) == 7


def get_diff_number_none_pure(arr: list):
    # this should be O(n) in time and O(1) in space
    n = len(arr)
    for idx in range(n):
        ptr = arr[idx]
        while ptr < n and arr[ptr] != ptr:
            tmp = arr[ptr]
            arr[ptr] = ptr
            ptr = tmp

    for idx in range(n):
        if arr[idx] != idx:
            return idx

    return n


assert get_diff_number_none_pure([0]) == 1
assert get_diff_number_none_pure([0, 1, 2]) == 3
assert get_diff_number_none_pure([1, 3, 0, 2]) == 4
assert get_diff_number_none_pure([100000]) == 0
assert get_diff_number_none_pure([1, 0, 3, 4, 5]) == 2
assert get_diff_number_none_pure([0, 999999]) == 1
assert get_diff_number_none_pure([0, 1, 4, 2, 5, 6, 3]) == 7
