# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Microsoft.
#
# Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does
# not necessarily have to be contiguous.
#
# For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing
# subsequence has length 6: it is 0, 2, 6, 9, 11, 15.

def LIS(arr: list) -> list:
    # GG: text book dynamic programming problem
    # O(n^2) in time, and O(n) in space
    if not list:
        return []
    elif len(arr) == 1:
        return arr

    # let L(i) be the length of longest increasing subseq from beginning of arry up to and actually include i-th
    # index in LIS then L(i) = max length of {L(0) ... L(j)} + 1, where 0 <= j < i, and array[j] < array[i]
    memo = [1] * len(arr)

    # init
    for i in range(1, len(arr)):
        existing_lis = [value for idx, value in enumerate(memo[:i]) if arr[idx] < arr[i]]
        if existing_lis:
            memo[i] = max(existing_lis) + 1

    # now backtrack to find the actual LIS
    cur_max_len = max(memo)
    res = [cur_max_len]
    for idx, val in enumerate(memo[::-1]):
        # print("idx: {}, val: {}".format(idx, val))
        if val == cur_max_len - 1:
            res.append(arr[len(arr) - idx])
            cur_max_len -= 1

    return res[::-1]


assert LIS([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == [0, 2, 6, 9, 11, 15]
