# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by LinkedIn.
#
# Determine whether a tree is a valid binary search tree.
#
# A binary search tree is a tree with two children, left and right, and satisfies the constraint that the key in the
# left child must be less than or equal to the root and the key in the right child must be greater than or equal to
# the root.

from common.treenode.MyBST import BstIntNode
import sys


def is_bst(root: BstIntNode) -> bool:
    def is_bst_recur(node: BstIntNode, my_min: int, my_max: int) -> bool:
        if node is None:
            return True
        is_valid = my_min < node.val < my_max
        return is_valid and is_bst_recur(node.left, my_min, node.val) and is_bst_recur(node.right, node.val, my_max)

    return is_bst_recur(root, -sys.maxsize, sys.maxsize)


#       3
#    2      6
#  1      5   8
#        4   7 9

a = BstIntNode(3)
b = BstIntNode(2)
c = BstIntNode(1)
d = BstIntNode(6)
e = BstIntNode(5)
f = BstIntNode(8)
g = BstIntNode(4)
h = BstIntNode(7)
i = BstIntNode(9)

assert is_bst(a)

a.left = c
a.right = b
assert not is_bst(a)

a.left = b
a.right = d
assert is_bst(a)

b.left = c
d.right = e
assert not is_bst(a)

d.left = e
d.right = f
e.left = g
f.left = h
f.right = i
assert is_bst(a)
