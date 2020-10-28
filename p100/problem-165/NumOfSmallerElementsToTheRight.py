# This problem was asked by Google.

# Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original input array.

# For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

# There is 1 smaller element to the right of 3
# There is 1 smaller element to the right of 4
# There are 2 smaller elements to the right of 9
# There is 1 smaller element to the right of 6
# There are no smaller elements to the right of 1

"""
3, 4, 6, 9, 1
            0
      *  1

cur_max = 9

let k be number of element to the right that's smaller
So my first idea is this, scan from right, with the first right element to have a 0 for its k value.
Then check 2nd right element. If it's bigger than last one, take that k value + 1. If it's smaller, keep scanning
right to find one that makes current element bigger, take that k value + 1.

This is still O(n^2) however.


Turns out this is wrong. See "6, 1, 2". Element 6 should have k value of 2, but both 1 and 2 have value of 0
"""


# GG: this is O(n^2) though. I thought about something like dynamic programing of LIS, but that's still O(n^2). A
#  better solution is to use binary search tree, self balancing even, with modification to keep count of num of nodes
#  beneath this node. Walk the list from right, insert into the bst in that order, and do a look up to record it maybe

def num_smaller_to_right(lis: list) -> list:
    assert lis

    n = len(lis)
    res = []
    for i in range(n):
        count = len([_ for _ in lis[i + 1:] if _ < lis[i]])
        res.append(count)
    return res


assert num_smaller_to_right([3, 4, 9, 6, 1]) == [1, 1, 2, 1, 0]
