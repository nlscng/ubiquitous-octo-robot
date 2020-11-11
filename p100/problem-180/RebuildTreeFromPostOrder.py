# This problem was asked by Google.
#
# Given the sequence of keys visited by a postorder traversal of a binary search tree, reconstruct the tree.
#
# For example, given the sequence 2, 4, 3, 8, 7, 5, you should construct the following tree:
#
#     5
#    / \
#   3   7
#  / \   \
# 2   4   8

"""
This is another classic bst problem. If given the post order traversal, the last element will always be a root for a
sub tree. Then, the 2nd last node will be the last node's left child if it's smaller, right child if larger than last
node.

This should be enough to recurse on.

[l .... r] and a parent node
parent.left = [l ... i] where val(i) < parent.val
parent.right = [i + 1 .... r] where val(i + 1) > parent.val
return int_node(r)

"""

from common.treenode.MyBST import IntNode


def rebuild_bst_post_order(lis: list) -> IntNode:
    # this should be O(n^2) at worst time complexity, O(1) for space
    assert lis
    n = len(lis)

    def recur(l: int, r: int) -> IntNode:
        # left and right, inclusive indices for the sublist this inner helper function is looking into the outer list

        # GG: this is tricky to think through, I was flipping between functional and imperial, between returning a node
        #  and building a tree for outer function. In the end I had this functional version.
        if l > r:
            return None
        elif l == r:
            return IntNode(lis[l])
        else:
            i = r - 1
            while i >= l and lis[i] > lis[r]:
                i -= 1

            this_node = IntNode(lis[r])
            this_node.left = recur(l, i)
            this_node.right = recur(i + 1, r - 1)
            return this_node

    root = recur(0, n - 1)
    return root


print(rebuild_bst_post_order([2, 4, 3, 8, 7, 5]))
