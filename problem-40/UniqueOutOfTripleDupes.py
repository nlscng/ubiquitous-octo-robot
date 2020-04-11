# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given an array of integers where every integer occurs three times except for one integer, which only occurs once,
# find and return the non-duplicated integer.
#
# For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.
#
# Do this in O(N) time and O(1) space.

def find_unique(arr: list):
    # this is O(n) in time but not O(1) in space, space is probably O(n) too
    if not list:
        return None

    count = dict()
    for a in arr:
        key = str(a)
        if key not in count:
            count[key] = 0
        count[key] = count[key] + 1

    for k in count:
        if count[k] == 1:
            return int(k)

    return None


assert find_unique([1, 1, 1, 3]) == 3

import sys


def find_unique_web_solution(arr: list, k: int):
    # not my solution, but this is O(n) in time and O(1) in space.
    # this uses bit counting/mask, very clever
    # I think there are other problems where bit masks can help reduce O(n) to O(1)
    NUM_BIT_INT = 8 * sys.getsizeof(int)  # getsizeof return number of bytes
    bit_counter = [0] * NUM_BIT_INT  # an array where the value v at index i means there's v times of the i-bit

    for i in range(NUM_BIT_INT):
        for j in range(len(arr)):
            bit_mask = 1 << i
            if bit_mask & arr[j] != 0:
                bit_counter[i] += 1

    num = 0
    for i in range(NUM_BIT_INT):
        if bit_counter[i] % k != 0:
            int_value_from_bit = 1 << i
            num += (bit_counter[i] % k) * int_value_from_bit

    return num

assert find_unique_web_solution([1, 1, 1, 3], 3) == 3
