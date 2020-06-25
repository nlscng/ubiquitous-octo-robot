# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Microsoft.
#
# Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one
# of '+', '−', '∗', or '/'.
#
# Given the root to such a tree, write a function to evaluate it.
#
# For example, given the following tree:
#
#     *
#    / \
#   +    +
#  / \  / \
# 3  2  4  5
# You should return 45, as it is (3 + 2) * (4 + 5).

from common.treenode.MyBST import MyBstNodeStringVal

'''
    *
   / \
  +    +
 / \  / \
3  2  4  5

'''

def bst_arithmetic(root: MyBstNodeStringVal) -> int:
    if not root or not isinstance(root, MyBstNodeStringVal):
        return 0

    # this looks like a post order processing
    def post_traverse(node: MyBstNodeStringVal) -> int:
        if node.left is None or node.right is None:
            return int(node.val)

        left_res = post_traverse(node.left)
        right_res = post_traverse(node.right)
        my_ops = {
            '+': left_res + right_res,
            '-': left_res - right_res,
            '*': left_res * right_res,
            '/': left_res // right_res
        }
        return my_ops[node.val]

    return post_traverse(root)


test_a = MyBstNodeStringVal('3')
assert bst_arithmetic(test_a) == 3

test_b = MyBstNodeStringVal('+')
b_1 = MyBstNodeStringVal('2')
b_2 = MyBstNodeStringVal('3')
test_b.left = b_1
test_b.right = b_2
assert bst_arithmetic(test_b) == 5

test_c = MyBstNodeStringVal('*')
c_left = MyBstNodeStringVal('+')
c_right = MyBstNodeStringVal('+')
c_left_left = MyBstNodeStringVal('3')
c_left_right = MyBstNodeStringVal('2')
c_right_left = MyBstNodeStringVal('4')
c_right_right = MyBstNodeStringVal('5')
test_c.left = c_left
test_c.right = c_right
c_left.left = c_left_left
c_left.right = c_left_right
c_right.left = c_right_left
c_right.right = c_right_right
assert bst_arithmetic(test_c) == 45

