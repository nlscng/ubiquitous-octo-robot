# This problem was asked by Affirm.
#
# Given a array of numbers representing the stock prices of a company in chronological order, write a function that
# calculates the maximum profit you could have made from buying and selling that stock. You're also given a number
# fee that represents a transaction fee for each buy and sell transaction.
#
# You must buy before you can sell the stock, but you can make as many transactions as you like.
#
# For example, given [1, 3, 2, 8, 4, 10] and fee = 2, you should return 9, since you could buy the stock at 1 dollar,
# and sell at 8 dollars, and then buy it at 4 dollars and sell it at 10 dollars. Since we did two transactions,
# there is a 4 dollar fee, so we have 7 + 6 = 13 profit minus 4 dollars of fees.


"""
Another trade stock for profit question, although this one is allowing trading for unlimited times, so maybe DP isn't
needed. Like other unlimited trade problem, perhaps I can solve this with walking through the price list.

Or perhaps the inclusion of fees turns this into a dynamic programming one.

And it looks like it does. Consider this increasing sequence of prices: 1, 4, 7, 10. Greedy algorithms will buy twice,
making profit with two fees if fee is less than 3.

Question 47 used as reference.

1, 3, 2, 8, 4, 10


"""

from typing import List


def trade_with_fees_greedy(prices: List[int], fee: int) -> int:
    assert prices and len(prices) > 1

    max_profit = 0
    cur_min = prices[0]
    n_trades = 0

    for p in prices[1:]:
        if p < cur_min:
            cur_min = p
        elif p - fee > cur_min:
            max_profit += p - cur_min - fee
            n_trades += 1
            cur_min = p

    return max_profit


assert trade_with_fees_greedy([1, 3, 2, 8, 4, 10], 2) == 9

# this next case fails on greedy version
assert trade_with_fees_greedy([1, 3, 2, 1, 4, 10], 2) == 7

"""
So given a i-th day, and j-th price, max profit would be 
p(i, j) = max {
    p(i - 1, j - 1), no purchase completed on that day, aka ignore price change, 
    max(p(m, m) + (price(i) - price(m) - 2)), 0 < m < i, assume we now hold stock of 
        price purchased on m day, we sell and make profit today 
} 
"""


# SEE: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/?currentPage=1&orderBy=most_votes&query=

def trade_with_fees(prices: List[int], fee: int) -> int:
    assert prices and len(prices) > 1

    n = len(prices)
    # A 2D memo table, where x-axis is the given price history per day, and y-axis is day 1, day 2, etc
    # So a p(i, j), max profit of i-th day
    memo = [[0 for _ in range(n)] for _ in range(n)]

    return 0
