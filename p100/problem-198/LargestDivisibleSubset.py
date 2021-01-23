# This problem was asked by Google.
#
# Given a set of distinct positive integers, find the largest subset such that every pair of elements in the subset (
# i, j) satisfies either i % j = 0 or j % i = 0.
#
# For example, given the set [3, 5, 10, 20, 21], you should return [5, 10, 20]. Given [1, 3, 6, 24], return [1, 3, 6,
# 24].

##Google
##SubsetSum
##DP
##DynamicProgramming

"""
This feels like a dp problem of a 2D memo table. I can have a table where both
the row and the column represent an element in the array, and have the cell
record a boolean for if the r and c value are mutually divisible.

This would be O(n^2) in time and space.

After googling, we can apparently reduce the space to O(n), by counting on the fact
that smaller divisor will be divide up larger divisible numbers. Essentially treat
this as a LIS DP problem, where condition add one to the number of the subset is
where or not two values are mutually divisible.
"""

