# This problem was asked by Google.
#
# Given an array of numbers and an index i, return the index of the nearest larger number of the number at index i,
# where distance is measured in array indices.
#
# For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.
#
# If two distances to larger numbers are the equal, then return any one of them. If the array at i doesn't have a
# nearest larger integer, then return null.
#
# Follow-up: If you can preprocess the array, can you do this in constant time?

"""
This should be easily done in linear time. I can scan from the left and right, find the next larger element from
both direction, track their index distance, and return one with the smaller distance.


"""


# GG: good clarification question to ask is there's always going to be at least one larger value, or can the given
#  index be looking at largest value already

def nearest_larger(array: list, idx: int) -> int:
    assert array
    n = len(array)
    lg_left_idx, lg_right_idx = n, -1
    value = array[idx]
    for i in range(n):
        # scan from left
        if i > idx and array[i] > value:
            lg_right_idx = i
            break

    for i in range(n):
        # scan from right
        if n - i - 1 < idx and array[n - i - 1] > value:
            lg_left_idx = n - i - 1
            break

    res = 0
    if lg_left_idx == n and lg_right_idx == -1:
        res = None
    elif lg_right_idx == -1:
        res = lg_left_idx
    elif lg_left_idx == n:
        res = lg_right_idx
    elif abs(idx - lg_right_idx) > abs(idx - lg_left_idx):
        res = lg_left_idx
    else:
        res = lg_right_idx

    return res


# assert nearest_larger([2, 2, 2, 2], 2) is None
assert nearest_larger([4, 3, 2, 1], 2) == 1
assert nearest_larger([1, 2, 3, 4], 2) == 3
assert nearest_larger([4, 1, 3, 5, 6], 0) == 3
