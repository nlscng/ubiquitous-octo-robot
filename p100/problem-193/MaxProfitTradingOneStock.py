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

def trade_one_stock_with_fees(prices: List[int], fee: int) -> int:
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


assert trade_one_stock_with_fees([1,3,2,8,4,10], 2) == 9
assert trade_one_stock_with_fees([1,3,2,1,4,10], 2) == 7
