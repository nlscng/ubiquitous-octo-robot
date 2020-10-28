# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# You are given an array of non-negative integers that represents a two-dimensional elevation map where each element
# is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.
#
# Compute how many units of water remain trapped on the map in O(N) time and O(1) space.
#
# For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
#
# Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth
# index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.


def rain_capacity(arr: list) -> int:
    if len(arr) < 3:
        return 0

    # SEE: this is with time of O(n) but not space of O(1) though
    def scan_for_max(a: list) -> list:
        cur_max = -999  # magic number
        res = []
        for i in a:
            if i > cur_max:
                cur_max = i
            res.append(cur_max)
        return res

    l_scan_max = scan_for_max(arr)
    r_scan_max = scan_for_max(arr[::-1])[::-1]

    cap = 0
    for i in range(len(arr)):
        height = arr[i]
        left_wall = l_scan_max[i]
        right_wall = r_scan_max[i]
        cap += min(left_wall - height, right_wall - height)

    return cap


assert rain_capacity([]) == 0
assert rain_capacity([3, 2]) == 0
assert rain_capacity([2, 1, 2]) == 1
assert rain_capacity([3, 0, 1, 3, 0, 5]) == 8
assert rain_capacity([3, 0, 5, 0, 2]) == 5
assert rain_capacity([1, 3, 2, 4, 1, 2, 0]) == 2


def calculate_trapped_water(walls):
    # SEE: the O(n) time and O(1) space, awesome solution
    # https://github.com/vineetjohn/daily-coding-problem/blob/master/solutions/problem_030.py
    if len(walls) < 3:
        return 0

    total_water_volume = 0

    left = 0
    right = len(walls) - 1
    left_max = 0
    right_max = 0

    while left <= right:
        if walls[left] < walls[right]:
            if walls[left] > left_max:
                left_max = walls[left]
            else:
                total_water_volume += left_max - walls[left]
            left += 1
        else:
            if walls[right] > right_max:
                right_max = walls[right]
            else:
                total_water_volume += right_max - walls[right]
            right -= 1

    return total_water_volume


assert calculate_trapped_water([1]) == 0
assert calculate_trapped_water([2, 1]) == 0
assert calculate_trapped_water([2, 1, 2]) == 1
assert calculate_trapped_water([4, 1, 2]) == 1
assert calculate_trapped_water([4, 1, 2, 3]) == 3
assert calculate_trapped_water([3, 0, 1, 3, 0, 5]) == 8
assert calculate_trapped_water([10, 9, 1, 1, 6]) == 10
assert calculate_trapped_water([1, 3, 2, 4, 1, 2, 0]) == 2
