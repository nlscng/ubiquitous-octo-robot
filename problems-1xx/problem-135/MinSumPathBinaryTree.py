# This question was asked by Apple.
#
# Given a binary tree, find a minimum path sum from root to a leaf.
#
# For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.
#
#   10
#  /  \
# 5    5
#  \     \
#    2    1
#        /
#      -1


"""
This should be solvable with a dfs tree search while keeping a current min sum

Ah this is a little more involved, I have to back-track to maintain paritial path sum

stack: 5R, 2
cur_sum: 15
max_sum: 15
seen: 10, 5L
"""
from common.treenode.MyBST import IntNode
import sys


# GG: basic back tracking tree problem, worth reviewing

def min_sum_bst(root: IntNode) -> int:
    assert root is not None

    walker = None
    stack = [root]
    cur_sum = 0
    cur_path = []
    min_sum = sys.maxsize
    seen = set()
    while len(stack) > 0:
        walker = stack.pop()
        seen.add(walker)
        cur_path.append(walker)
        cur_sum += walker.val

        if walker.right is not None:
            stack.append(walker.right)
        if walker.left is not None:
            stack.append(walker.left)

        if walker.left is None and walker.right is None:
            # we've reached a leaf
            min_sum = min(cur_sum, min_sum)
            # start back tracking
            end = cur_path[-1]
            while len(cur_path) > 1 and (end.left is None or end.left in seen) and (
                    end.right is None or end.right in seen):
                cur_path.pop()
                cur_sum -= end.val
                end = cur_path[-1]

    return min_sum


a = IntNode(10)
b = IntNode(5)
c = IntNode(5)
d = IntNode(2)
e = IntNode(1)
f = IntNode(-1)
a.left = b
b.right = d
a.right = c
c.right = e
e.left = f
assert min_sum_bst(a) == 15
