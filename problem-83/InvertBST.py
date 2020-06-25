# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Invert a binary tree.
#
# For example, given the following tree:
#
#     a
#    / \
#   b   c
#  / \  /
# d   e f
# should become:
#
#   a
#  / \
#  c  b
#  \  / \

from common.treenode.MyBST import BstStrNode


def invert_bst(root: BstStrNode) -> BstStrNode:
    if root is None:
        return root

    root.left, root.right = root.right, root.left

    invert_bst(root.left)
    invert_bst(root.right)
    return root


a = BstStrNode('a')
b = BstStrNode('b')
c = BstStrNode('c')
d = BstStrNode('d')
e = BstStrNode('e')
f = BstStrNode('f')

a_copy = a.deepcopy()
assert invert_bst(a) == a_copy

a.reset()
b.reset()
a_copy.reset()
a_copy = a.deepcopy()
b_copy = b.deepcopy()
a.left = b
a_copy.right = b_copy
assert invert_bst(a) == a_copy

a.reset()
b.reset()
a_copy = a.deepcopy()
b_copy = b.deepcopy()
c_copy = c.deepcopy()
a.left = b
a.right = c
a_copy.right = b_copy
a_copy.left = c_copy
assert invert_bst(a) == a_copy

a.reset()
b.reset()
a_copy = a.deepcopy()
b_copy = b.deepcopy()
c_copy = c.deepcopy()
d_copy = d.deepcopy()
e_copy = e.deepcopy()
f_copy = f.deepcopy()

a.left = b
b.left = d
b.right = e
a.right = c
c.left = f

a_copy.left = c_copy
c_copy.right = f_copy
a_copy.right = b_copy
b_copy.left = e_copy
b_copy.right = d_copy

assert invert_bst(a) == a_copy
