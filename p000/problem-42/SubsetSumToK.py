# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If
# such a subset cannot be made, then return null.
#
# Integers can appear more than once in the list. You may assume all numbers in the list are positive.
#
# For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.

## DynamicPrograming
## DP


def subset_sum(arr: list, k: int):
    if not isinstance(arr, list):
        raise Exception("Expected an array, got {} instead.".format(type(arr)))
    if not arr:
        return []

    # init clean, this turns out to be more important than I realized
    cleaned = [x for x in arr if x <= k]

    n = len(cleaned)
    # note the +1 on width and height
    memo = [[False] * (k + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        memo[i][0] = True

    for i in range(1, len(memo)):
        for j in range(1, len(memo[0])):
            value_i = cleaned[i - 1]
            memo[i][j] = memo[i - 1][j - value_i] or memo[i - 1][j] if j - value_i >= 0 else False

    # retract to find our path
    sol = []
    if not memo[n][k]:
        return None

    walker = (row, col) = (n, k)
    leftover = k
    while leftover > 0:
        item_value = cleaned[row - 1]
        included_item = memo[row - 1][col - item_value]
        # not_included_item = memo[row - 1][col]
        if included_item:
            leftover -= item_value
            sol.append(cleaned[row - 1])
            row -= 1
            col -= item_value
        else:
            row -= 1

    return sol[::-1]


# assert subset_sum([], 4) == []
# assert subset_sum([3], 3) == [3]
# assert subset_sum([1, 1, 1], 3) == [1, 1, 1]
# assert subset_sum([1,2,5,3,4], 9) == []
assert set(subset_sum([12, 1, 61, 5, 9, 2], 24)) == {12, 9, 2, 1}
