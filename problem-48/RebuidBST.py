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


class MyBstNode:
    def __init__(self, val: str, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        res = self.val
        if self.left is not None:
            res = res + ", " + str(self.left)
        if self.right is not None:
            res = res + ", " + str(self.right)
        return res

    def __eq__(self, other):
        if other is None or not isinstance(other, MyBstNode):
            return False
        return self.val == other.val and self.left == other.left and self.right == other.right


a = MyBstNode('a')
b = MyBstNode('b')
c = MyBstNode('c')
d = MyBstNode('d')
a.left = b
a.right = c
# b.parent = a
# c.parent = a
b.left = d
# d.parent = b
assert str(a) == 'a, b, d, c'


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
            return MyBstNode(idx_to_val[pre[0]])

        head = pre[0]
        rest = pre[1:]
        left, right = split(head, rest)
        left_child = build(left)
        right_child = build(right)
        root = MyBstNode(idx_to_val[head])
        root.left = left_child
        root.right = right_child
        return root

    indices = [val_to_idx[x] for x in preorder]
    tree = build(indices)
    return tree


a = MyBstNode('a')
b = MyBstNode('b')
c = MyBstNode('c')
d = MyBstNode('d')
e = MyBstNode('e')
f = MyBstNode('f')
g = MyBstNode('g')

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
