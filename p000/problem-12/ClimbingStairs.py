# This problem was asked by Amazon.
#
# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N,
# write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.
#
# For example, if N is 4, then there are 5 unique ways:
#
# 1, 1, 1, 1 2, 1, 1 1, 2, 1 1, 1, 2 2, 2 What if, instead of being able to climb 1 or 2 steps at a time,
# you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3,
# or 5 steps at a time.


def climb_stairs_with_one_and_two(total: int):
    if total == 0:
        return 0
    elif total == 1:
        return 1
    elif total == 2:
        return 2
    ways = [0] * (total + 1)

    ways[0] = 1
    ways[1] = 1
    ways[2] = 2

    for i in range(3, total + 1):
        ways[i] = ways[i - 1] + ways[i - 2]

    return ways[-1]


assert climb_stairs_with_one_and_two(4) == 5


def climb_stairs(total: int, step_sizes: []):
    if not step_sizes or not total:
        return 0

    memo = [0] * (total + 1)
    for s in step_sizes:
        if s < total:
            memo[s] = 1

    for i in range(total + 1):
        for s in step_sizes:
            if i - s > 0:
                memo[i] += memo[i - s]

    return memo[-1]


assert climb_stairs(4, [1, 2]) == 5
assert climb_stairs(4, [1, 3, 5]) == 3
assert climb_stairs(4, [1, 3]) == 3
assert climb_stairs(5, [1, 3, 5]) == 4
