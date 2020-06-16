# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given a array of numbers representing the stock prices of a company in chronological order, write a function that
# calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you
# can sell it.
#
# For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell
# it at 10 dollars.
import sys


def trade_once(prices: list) -> int:
    if not prices or len(prices) < 2:
        return 0

    max_profit = 0
    cur_min = prices[0]

    for one_price in prices[1:]:
        if one_price > cur_min:
            max_profit = max(max_profit, one_price - cur_min)
        if one_price < cur_min:
            cur_min = one_price

    return max_profit


assert trade_once([9]) == 0
assert trade_once([9, 11, 8, 5, 7, 10]) == 5
assert trade_once([3, 0, 9, 4, 7, 2, 1]) == 9
assert trade_once([1, 2, 3, 4, 5]) == 4
assert trade_once([1, 1, 1, 1, 1]) == 0
assert trade_once([1, 1, 1, 2, 1]) == 1
assert trade_once([5, 4]) == 0
