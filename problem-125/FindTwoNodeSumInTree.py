# This problem was asked by Google.
#
# Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.
#
# For example, given the following tree and K of 20
#
#     10
#    /   \
#  5      15
#        /  \
#      11    15
# Return the nodes 5 and 15.

"""
Naive solution that is O(n), first flatten the tree, doesn't matter if it's pre or post order, bfs or dfs, then finding
two sum to k in that flattened list is another O(n)

Better solution, maybe, is two walkers. A left and right walker, both start at root. If sum of the two walker adds to k,
then we found the nodes. Otherwise, if smaller than k, move

As two walkers walks down the two branches, keep a record of target remaining number like the regular two sum problem.


walk through the given example
  l:10, 5,
  r:10, *,
set:10, 15
"""

from common.treenode.MyBST import IntNode


def two_sum_tree(root: IntNode, k: int) -> []:
    # this is O(n) in time and O(n) in space
    if not root:
        return []

    # bfs down the tree while keeping a target set
    walker = root
    queue = [walker]
    target = set()

    while len(queue) > 0:
        walker = queue.pop(0)
        if walker.val in target:
            return sorted([walker.val, k - walker.val])
        else:
            target.add(k - walker.val)

        if walker.left is not None:
            queue.append(walker.left)
        if walker.right is not None:
            queue.append(walker.right)

    return []


a = IntNode(10)
b = IntNode(5)
c = IntNode(15)
d = IntNode(11)
e = IntNode(15)

a.left = b
a.right = c
c.left = d
c.right = e

assert two_sum_tree(a, 20) == [5, 15]
assert two_sum_tree(a, 30) == [15, 15]
assert two_sum_tree(a, 2) == []


