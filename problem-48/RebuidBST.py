# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.
#
# For example, given the following preorder traversal:
#
# [a, b, d, e, c, f, g]
#
# And the following inorder traversal:
#
# [d, b, e, a, f, c, g]
#
# You should return the following tree:
#     a
#    / \
#   b   c
#  / \ / \
# d  e f  g

from common.treenode.MyBstNodeStringVal import MyBstNodeStringVal


def build_tree(preorder: list, inorder: list):
    if not isinstance(preorder, list) or not isinstance(inorder, list):
        return None
    if not preorder or not inorder:
        return None

    # grab first from the pre order list, this is the node we create and ultimately return
    # use in order list, find the node, and a list of everything to the left, and a list of everything to the right
    # call the build function twice, one with the list to the left, one with list to the right, and set the main.left
    # to the result of left list call, set main.right to result of right list call
    # profit

    idx_to_val = {idx: value for idx, value in enumerate(inorder)}
    val_to_idx = {idx_to_val[k]: k for k in idx_to_val}

    def split(pt: int, pre: list):
        '''
        Given a position, and a pre-order list, split indices in the given 'pre' list that is in-orderly on the left and
        right of it
        :param pt:
        :param liz:
        :return: two list of int indices, first for indices that's on the left, second on the right of the pt
        '''
        left = [x for x in pre if x < pt]
        right = [x for x in pre if x > pt]
        return left, right

    def build(pre: list):
        if not pre:
            return None
        if len(pre) == 1:
            return MyBstNodeStringVal(idx_to_val[pre[0]])

        head = pre[0]
        rest = pre[1:]
        left, right = split(head, rest)
        left_child = build(left)
        right_child = build(right)
        root = MyBstNodeStringVal(idx_to_val[head])
        root.left = left_child
        root.right = right_child
        return root

    indices = [val_to_idx[x] for x in preorder]
    tree = build(indices)
    return tree


a = MyBstNodeStringVal('a')
b = MyBstNodeStringVal('b')
c = MyBstNodeStringVal('c')
d = MyBstNodeStringVal('d')
e = MyBstNodeStringVal('e')
f = MyBstNodeStringVal('f')
g = MyBstNodeStringVal('g')

assert build_tree([], []) is None
assert build_tree(['a'], ['a']) == a

a.left = b
assert build_tree(['a', 'b'], ['b', 'a']) == a

a.right = c
assert build_tree(['a', 'b', 'c'], ['b', 'a', 'c']) == a

b.left = d
b.right = e
c.left = f
c.right = g
assert build_tree(['a', 'b', 'c', 'd', 'e', 'f', 'g'], ['d', 'b', 'e', 'a', 'f', 'c', 'g']) == a
