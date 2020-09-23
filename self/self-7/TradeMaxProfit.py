# This problem was asked by Facebook.
#
# Given an array of numbers representing the stock prices of a company in chronological order and an integer k,
# return the maximum profit you can make from k buys and sells. You must buy the stock before you can sell it,
# and you must sell the stock before you can buy it again.
#
# For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.

"""
this is similar to a trade once max profit problem, see problem 47, but different since we can trade multiple times.
Only caveat is you can only hold one stock max at one time.

Maybe the linear idea still works? I can scan backward to find current max given an element. That is, for an element,
the max value to its right. So the diff can give me profit. Then at the end, sum up the positive diffs?

5, 2, 4, 0, 1
4, 4, 1, 1, 0
*, 2, *, 1, *

This doesn't work, the below example breaks it, as consecutive increases will double dip the profit. Hmm.

3, 1, 5, 8, 2, 7
8, 8, 8, 7, 7, *(max to right)

So after a scan for "max to right", walk through the list again, when the max-to-right changes, it means we are actually
selling, so take the profit


3, 1, 5, 8, 2, 7 prices
8, 8, 8, 7, 7, 0 max sale possible
               *

cur min cost = 7
cur max sale = 0
total profit = 12
"""


# GG: this is very tricky to get entirely correct, worthy of an interview question
# GG: I messed up, I did this ignoring k, so this is essentially trade any number of times while maxing profit
#  This was original daily coding problem 130


def trade_max_profit(prices: list) -> int:
    # this is O(n) in time and O(n) in space
    assert len(prices) > 1
    n = len(prices)
    max_that_day_backward = [0]
    cur_max_profit = 0
    for p in prices[1:][::-1]:
        cur_max_profit = max(cur_max_profit, p)
        max_that_day_backward.append(cur_max_profit)

    assert len(max_that_day_backward) == n
    max_sale_possible = max_that_day_backward[::-1]

    cur_min_cost = prices[0]
    cur_max_sale = max_sale_possible[0]
    total_profit = 0
    for i in range(1, n):
        if cur_max_sale != max_sale_possible[i] or cur_min_cost < prices[i]:
            # we are making a sale
            if prices[i] > cur_min_cost:
                total_profit += prices[i] - cur_min_cost
            cur_min_cost = prices[i]
            cur_max_sale = max_sale_possible[i]
        else:
            cur_min_cost = min(cur_min_cost, prices[i])

    return total_profit


assert trade_max_profit([5, 2, 4, 0, 1]) == 3
assert trade_max_profit([3, 1, 5, 8, 2, 7]) == 12
assert trade_max_profit([5, 4, 2, 1]) == 0
assert trade_max_profit([3, 5, 3, 5, 3, 5]) == 6, "Actual: {}".format(trade_max_profit([3, 5, 3, 5, 3, 5]))
assert trade_max_profit([3, 1, 3, 1, 3, 1]) == 4, "Actual: {}".format(trade_max_profit([3, 1, 3, 1, 3, 1]))
assert trade_max_profit([2, 5, 4, 2, 1]) == 3
