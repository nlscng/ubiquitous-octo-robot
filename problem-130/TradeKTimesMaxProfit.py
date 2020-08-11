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

let p be maximum profit possible on ith day with k purchase completed.
p(i, k) = max p(0 ... i-1, k -1) +
"""

# TBC