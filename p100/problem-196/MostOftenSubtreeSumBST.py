# This problem was asked by Apple.
#
# Given the root of a binary tree, find the most frequent subtree sum. The subtree sum of a node is the sum of all values under a node, including the node itself.
#
# For example, given the following tree:
#
#   5
#  / \
# 2  -5
# Return 2 as it occurs twice: once as the left leaf, and once as the sum of 2 + 5 - 5.

"""
Another variation of BST traversal that should benefit from bubbling things back up to root.
"""

from common.treenode.MyBST import IntNode
from collections import defaultdict


def most_frequent_sum_bst(root: IntNode) -> int:
    # This should be O(n) in time and space, n being the number of nodes in the tree, since we visit
    # each node one time before passing back up.
    assert root
    counts: defaultdict = defaultdict(int)  # a dictionary of sum:count key-value pairs

    def traverse(node: IntNode) -> int:
        left_sum = traverse(node.left) if node.left is not None else 0
        right_sum = traverse(node.right) if node.right is not None else 0
        my_sum = node.val + left_sum + right_sum
        counts[my_sum] += 1
        return my_sum

    traverse(root)
    return max([v for (k, v) in counts.items()])


c = IntNode(-5)
b = IntNode(2)
a = IntNode(5, b, c)
# assert most_frequent_sum_bst(a) == 2

#        -3
#   -2       -1
# 4   1    2    2
# 4 1 2 2, 3, 3, 3
g = IntNode(2)
f = IntNode(2)
e = IntNode(1)
d = IntNode(4)
c = IntNode(-1, f, g)
b = IntNode(-2, d, e)
a = IntNode(-3, b, c)
assert most_frequent_sum_bst(a) == 3, "Actual: {}".format(most_frequent_sum_bst(a))
