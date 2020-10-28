# This problem was asked by Google.
#
# Find the minimum number of coins required to make n cents.
#
# You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.
#
# For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.

"""
This is a classic dynamic programming problem. Another flavor is that there are limited number of each coin.

To start, I am thinking we will need a 2D table, x axis will be the combined value with current coin compositions,
and y axis will be each individual coin.

So let c(i, j) be the minimum number of coin to represent j dollar, using 0th, 1st, 2nd.. i-th type of coin so far.
Let v(i) be the face value of coin type i.
Then c(i, j) =
            min (
            c(i - 1, j - v(1)) + 1,
            c(i - 1, j - v(2)) + 1,
            ...
            c(i - 1, j - v(i)) + 1
            )

n = 16,
k = 3, with a 10, 5 and 1

"""

# GG: first version was a 2D memo table, but this can be optimized to use memory of just O(n). Pretty tricky, but sweet

coins = [1, 5, 10, 25]


def coin_change(n: int) -> int:
    # Optimized version is O(n * c) in time, but O(n) in space, where n is target sum and c is number of type of coins
    assert n > 0
    k = 0
    n_coin_type = len(coins)
    memo = [i for i in range(n + 1)]

    for i in range(1, len(memo)):
        for coin_value in coins:
            if coin_value <= i:
                memo[i] = memo[i - coin_value] + 1
    return memo[-1]


assert coin_change(3) == 3
assert coin_change(5) == 1
assert coin_change(10) == 1
assert coin_change(16) == 3
assert coin_change(11) == 2
assert coin_change(42) == 5
assert coin_change(98) == 8
