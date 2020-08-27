# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
#
# For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements
# 42, 14, -5, and 86.
#
# Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.
#
# Do this in O(N) time.

def find_max_sum_subarray(arr: list) -> int:
    f_ptr, s_ptr = 0, 0  # fast ptr, slow ptr

    cur_max = 0
    while s_ptr < len(arr):
        if arr[s_ptr] >= 0:
            # found a base, start scanning
            f_ptr = s_ptr + 1
            cur_sum = arr[s_ptr]
            while f_ptr < len(arr) and cur_sum + arr[f_ptr] > 0:
                cur_sum += arr[f_ptr]
                f_ptr += 1
            if cur_sum > cur_max:
                cur_max = cur_sum
            s_ptr = f_ptr
        else:
            s_ptr += 1

    return cur_max


assert find_max_sum_subarray([1, -1, 1, -1]) == 1
assert find_max_sum_subarray([1, 2, 0, 3, 4]) == 10
assert find_max_sum_subarray([34, -50, 42, 14, -5, 86]) == 137
assert find_max_sum_subarray([-5, -1, -8, -9]) == 0
