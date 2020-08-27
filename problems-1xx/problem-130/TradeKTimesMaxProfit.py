# This problem was asked by Facebook.
#
# Given an array of numbers representing the stock prices of a company in chronological order and an integer k,
# return the maximum profit you can make from k buys and sells. You must buy the stock before you can sell it,
# and you must sell the stock before you can buy it again.
#
# For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.


"""
This feels like a DP problem. A 2D memo, where x axis holds the price (or some other value, profit maybe?)
and y axis holds number of purchases (or maybe number of transaction, aka buy, sell)

     8, 8, 8, 7, 7, 0 (upcoming max)
     3, 1, 5, 8, 2, 7 (prices)
1st
2nd

let p be maximum profit possible on ith day with j purchase completed.
p(i, j) = max of the two scenario:
    p(i, j -1), the same profit as the day before if we dont complete any transactions on j day
    p(i - 1, m) + (price(j) - price(m)), 0 < m < j, we sell (and assume we bought on m day)
"""

# GG: review this, this trade for max profit with k transaction is the hardest in the trade for profit, where trade
#  once and unlimited are both eaiser
#  See self-7 for unlimited trade, and problem-47 for trading just once

import sys


def trade_k_times(prices: list, k: int) -> int:
    # this version, keeping the 'currently seen max possible profit from past', is O(kn) in time, and O(kn) in space
    assert len(prices) > 1 and k > 0
    n = len(prices)

    memo = [[0 for _ in range(n)] for _ in range(k + 1)]  # note the k goes from 0 to k transaction
    assert len(memo) == k + 1 and len(memo[0]) == n

    for i in range(1, k + 1):
        cur_max = -sys.maxsize
        for j in range(1, n):
            ## the O(k n^2) version
            # possible_profit = max([prices[j] - prices[m] + memo[i - 1][m] for m in range(0, j)])

            ## the O(kn) version
            cur_max = max(cur_max, memo[i - 1][j - 1] - prices[j - 1])
            possible_profit = prices[j] + cur_max
            
            memo[i][j] = max(memo[i][j - 1], possible_profit)

    return memo[k][n - 1]


assert trade_k_times([5, 2, 4, 0, 1], 2) == 3, "Actual: {}".format(trade_k_times([5, 2, 4, 0, 1], 2))
assert trade_k_times([3, 1, 5, 8, 2, 7], 2) == 12, "Actual: {}".format(trade_k_times([3, 1, 5, 8, 2, 7], 2))
assert trade_k_times([3, 5, 3, 5, 3, 5], 2) == 4
