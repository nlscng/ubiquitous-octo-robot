# This question was asked by BufferBox.
#
# Given a binary tree where all nodes are either 0 or 1, prune the tree so that subtrees containing all 0s are removed.
#
# For example, given the following tree:
#
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  0   0
# should be pruned to:
#
#    0
#   / \
#  1   0
#     /
#    1
# We do not remove the tree at the root or its left child because it still has a 1 as a descendant.


"""
This looks like a good review of tree traversal.
"""

from common.treenode.MyBST import IntNode


def prune_zero_sub(root: IntNode) -> IntNode:
    # This should be time O(n) and space O(1), we go post order traversal through the tree one time, and prune away

    assert root

    def is_staying(node: IntNode) -> bool:
        assert node
        is_left_staying, is_right_staying = False, False
        if node.left is not None:
            is_left_staying = is_staying(node.left)
            if not is_left_staying:
                node.left = None
        if node.right is not None:
            is_right_staying = is_staying(node.right)
            if not is_right_staying:
                node.right = None

        res = node.val == 1 or is_left_staying or is_right_staying
        return res

    is_staying(root)
    return root


a = IntNode(0)
b = IntNode(1)
c = IntNode(0)
d = IntNode(1)
e = IntNode(0)
f = IntNode(0)
g = IntNode(0)
a.left = b
a.right = c
c.left = d
c.right = e
d.left = f
d.right = g
print(prune_zero_sub(a))

