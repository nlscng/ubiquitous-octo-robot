# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given a binary tree of integers, find the maximum path sum between two nodes. The path must go through at least one
# node, and does not need to go through the root.

from common.treenode.MyBST import MyBstNodeIntVal


def max_sum_path(root: MyBstNodeIntVal) -> int:
    cur_max = [0]  # using a object, in this case a list, reference so it's mutable from inner function

    def recur(node: MyBstNodeIntVal):
        # given a node in the tree, there a few scenario
        # 1. this node is used with sum from left child
        # 2. this node is used with sum from right child
        # 3. this node is used by itself
        # 4. this node is used with both left and right child sum (this case we don't pass back up, we store in cur_max
        if node is None:
            return 0

        l_res = recur(node.left)
        r_res = recur(node.right)
        res_max = max(node.val + l_res, node.val + r_res, node.val, 0)
        cur_max[0] = max(node.val + l_res + r_res, res_max, cur_max[0])

        return res_max

    _ = recur(root)
    return cur_max[0]


a = MyBstNodeIntVal(3)
b = MyBstNodeIntVal(2)
c = MyBstNodeIntVal(1)
#   3
assert max_sum_path(a) == 3

a.left = b
a.right = c
#   3
#  2 1
assert max_sum_path(a) == 6

#     3
#  2     1
# 4 2   1  3
d = MyBstNodeIntVal(4)
e = MyBstNodeIntVal(2)
f = MyBstNodeIntVal(1)
g = MyBstNodeIntVal(3)
b.left = d
b.right = e
c.left = f
c.right = g
assert max_sum_path(a) == 13, "actual: {}".format(max_sum_path(a))

#    -3
#  2     1
# 4 2   1  3
a.val = -3
assert max_sum_path(a) == 8, "actual: {}".format(max_sum_path(a))


#     0
#   2    -1
#-99 2   1  3
a.val = 0
d.val = -99
c.val = -1
assert max_sum_path(a) == 6, "actual: {}".format(max_sum_path(a))

#     0
#   2     1
#-99 2  -1 -1
c.val = 1
g.val = f.val = -1
assert max_sum_path(a) == 5, "actual: {}".format(max_sum_path(a))
