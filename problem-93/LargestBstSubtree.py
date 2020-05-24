# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Apple.
#
# Given a tree, find the largest tree/subtree that is a BST.
#
# Given a tree, return the size of the largest tree/subtree that is a BST.
from common.treenode.MyBST import MyBstNodeIntVal
import sys


def largest_bst_subtree(root: MyBstNodeIntVal) -> bool:
    def recur(node: MyBstNodeIntVal) -> (bool, int, int, int):
        if node is None:
            # GG: watch out for the positive min and negative max, it's done so all future boundary check is valid
            return True, 0, sys.maxsize, -sys.maxsize
        if node.left is None and node.right is None:
            return True, 1, node.val, node.val

        l_is_bst, l_bst_size, l_min, l_max = recur(node.left)
        r_is_bst, r_bst_size, r_min, r_max = recur(node.right)

        is_bst = l_is_bst and r_is_bst and l_max < node.val < r_min
        cur_min = -sys.maxsize
        cur_max = sys.maxsize
        if is_bst:
            bst_size = l_bst_size + r_bst_size + 1
            cur_min, cur_max = l_min, r_max
        elif l_is_bst:
            bst_size = l_bst_size
            cur_min, cur_max = l_min, r_max
        elif r_is_bst:
            bst_size = r_bst_size
        else:
            bst_size = 0

        return is_bst, bst_size, cur_min, cur_max

    _, size_largest_bst_sub, _, _ = recur(root)
    return size_largest_bst_sub


a = MyBstNodeIntVal(1)
b = MyBstNodeIntVal(2)
c = MyBstNodeIntVal(3)
d = MyBstNodeIntVal(4)
e = MyBstNodeIntVal(5)
# single note tree
assert largest_bst_subtree(a) == 1

#   2
#  1
b.left = a
a.parent = b
assert largest_bst_subtree(b) == 2

#  1
#   2
a.reset()
b.reset()
a.right = b
b.parent = a
assert largest_bst_subtree(a) == 2

#  2
# 1 3
a.reset()
b.reset()
c.reset()
b.left = a
b.right = c
assert largest_bst_subtree(b) == 3

#    3
#   2  4
# 1      5
b.reset()
c.left = b
b.left = a
c.right = d
d.right = e
assert largest_bst_subtree(c) == 5

#    3
#   2  4
# 1   5
a.reset()
b.reset()
c.reset()
d.reset()
e.reset()
c.left = b
b.left = a
c.right = d
d.left = e
assert largest_bst_subtree(c) == 2
