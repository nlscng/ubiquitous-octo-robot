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

from common.treenode.MyBST import BstStrNode

'''
    *
   / \
  +    +
 / \  / \
3  2  4  5

'''

def bst_arithmetic(root: BstStrNode) -> int:
    if not root or not isinstance(root, BstStrNode):
        return 0

    # this looks like a post order processing
    def post_traverse(node: BstStrNode) -> int:
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


test_a = BstStrNode('3')
assert bst_arithmetic(test_a) == 3

test_b = BstStrNode('+')
b_1 = BstStrNode('2')
b_2 = BstStrNode('3')
test_b.left = b_1
test_b.right = b_2
assert bst_arithmetic(test_b) == 5

test_c = BstStrNode('*')
c_left = BstStrNode('+')
c_right = BstStrNode('+')
c_left_left = BstStrNode('3')
c_left_right = BstStrNode('2')
c_right_left = BstStrNode('4')
c_right_right = BstStrNode('5')
test_c.left = c_left
test_c.right = c_right
c_left.left = c_left_left
c_left.right = c_left_right
c_right.left = c_right_left
c_right.right = c_right_right
assert bst_arithmetic(test_c) == 45

