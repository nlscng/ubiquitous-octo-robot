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
coins = [1, 5, 10, 25]

def coin_change(n: int) -> int:
    assert n > 0
    k = 0
    n_coin_type = len(coins)
    memo = [[0 for _ in range(n+1)] for _ in range(n_coin_type)] # note the col, the money value is 1 indexed

    # init the first row, where all cell are coins needed to count for x value with just the 1 cent coin
    for i in range(len(memo[0])):
        memo[0][i] = i

    for r in range(1, len(memo)):
        for c in range(1, len(memo[0])):
            coin_value = coins[r]
            if coin_value > c:
                memo[r][c] = memo[r -1][c]
            else:
                memo[r][c] = memo[r][c - coin_value] + 1
    return memo[n_coin_type - 1][n]


assert coin_change(3) == 3
assert coin_change(5) == 1
assert coin_change(10) == 1
assert coin_change(16) == 3
assert coin_change(11) == 2
assert coin_change(42) == 5
assert coin_change(98) == 8
