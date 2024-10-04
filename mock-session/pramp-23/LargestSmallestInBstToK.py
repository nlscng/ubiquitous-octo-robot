# Largest Smaller BST Key Given a root of a Binary Search Tree (BST) and a number num, implement an efficient
# function findLargestSmallerKey that finds the largest key in the tree that is smaller than num. If such a number
# doesn’t exist, return -1. Assume that all keys in the tree are nonnegative.
#
# Analyze the time and space complexities of your solution.
#
# For example:
#
# For num = 17 and the binary search tree below:
#
#        20
#      /    \
#    9        25
#   /  \
# 5     12
#      /  \
#     11   14
#
# Your function would return: 14 since it’s the largest key in the tree that is still smaller than 17.

"""
I struggled to get this idea in time during pramp.

k = 17
last_val: n, 20
walker:   20, 9,
"""

from common.treenode.MyBST import IntNode


# GG: very tricky to think through all the cases, but worth the exercise. Another thing, the presence of equal sign
#  is super important in places

def largest_smaller(root: IntNode, k: int) -> int:
    assert root is not None
    if root.left is None and root.right is None:
        return -1

    last_val = None
    walker = root

    while (walker.val >= k and walker.left is not None) or (walker.val <= k and walker.right is not None):
        # the equal signs in two logic branches are important, coz if walker walks onto k, we want to keep
        # going down the tree if there are child branches.
        if walker.val >= k:
            last_val = walker.val
            walker = walker.left
        else:
            last_val = walker.val
            walker = walker.right

    # now we have gone as far as we can down the tree, the given number may or may not be enclosed by walker and last
    # val
    if last_val <= k < walker.val:
        # the greater than, but not greater or equal to, is important here. If walker is the given value, it's handled
        # by the following branches
        return min(last_val, walker.val)
    elif k > walker.val:
        return walker.val
    else:
        return -1


a = IntNode(20)
assert largest_smaller(a, 17) == -1
b = IntNode(9)
c = IntNode(25)
d = IntNode(5)
e = IntNode(12)
f = IntNode(11)
g = IntNode(14)
a.left = b
a.right = c
b.left = d
b.right = e
e.left = f
e.right = g
assert largest_smaller(a, 17) == 14
assert largest_smaller(a, 12) == 11
assert largest_smaller(a, 6) == 5
assert largest_smaller(a, 30) == 25
assert largest_smaller(a, 4) == -1
assert largest_smaller(a, 5) == -1
