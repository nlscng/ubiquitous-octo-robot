#
# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Dropbox.
#
# Given the root to a binary search tree, find the second largest node in the tree.

class NodeBST:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def find_second_largest(node: NodeBST):
    flatten = []
    in_order(node, flatten)

    return flatten[-2] if len(flatten) > 2 else None


def in_order(node: NodeBST, accu: []):
    if node is None:
        return

    if node.left is not None:
        in_order(node.left, accu)

    accu.append(node.value)

    if node.right is not None:
        in_order(node.right, accu)


def find_nth_largest(node: NodeBST, nth: int):
    flatten = []
    in_order(node, flatten)

    return flatten[-nth] if len(flatten) > nth else None


test_tree_a = NodeBST(3,
                      NodeBST(1,
                              right=NodeBST(2)),
                      NodeBST(4,
                              right=NodeBST(5)))

assert find_second_largest(test_tree_a) == 4
assert find_nth_largest(test_tree_a, 2) == 4
assert find_nth_largest(test_tree_a, 6) is None
