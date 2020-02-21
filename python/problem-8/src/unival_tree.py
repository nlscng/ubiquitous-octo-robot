
def count_unival_tree(root):
    """
    A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

    Given the root to a binary tree, count the number of unival subtrees.
    :param root: a root of a tree
    :return: int, for the count of number of unival subtrees detected
    """
    if root is None:
        return 0

    left_count = count_unival_tree(root.left)
    right_count = count_unival_tree(root.right)
    if is_unival(root):
        return 1 + left_count + right_count
    else:
        return left_count + right_count


def is_unival(root):
    if root is None:
        return True

    if root.right is not None and root.val != root.right.val:
        return False

    if root.left is not None and root.val != root.left.val:
        return False

    if is_unival(root.left) and is_unival(root.right):
        return True

    return False

class UnivalTreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# test cases
test_tree_a = UnivalTreeNode(0,
                           UnivalTreeNode(1, None, None),
                           UnivalTreeNode(0,
                                          UnivalTreeNode(1,
                                                         UnivalTreeNode(1, None, None),
                                                         UnivalTreeNode(1, None, None)),
                                          UnivalTreeNode(0, None, None)))

test_tree_single = UnivalTreeNode(0, None, None)
test_tree_two_level_uni = UnivalTreeNode(0, UnivalTreeNode(0, None, None), UnivalTreeNode(0, None, None))
test_tree_two_level_dual = UnivalTreeNode(0, UnivalTreeNode(1, None, None), UnivalTreeNode(0, None, None))

# test the helper function that detect whether a tree is unival
assert is_unival(test_tree_single)
assert is_unival(test_tree_two_level_uni)
assert not is_unival(test_tree_two_level_dual)

# test count unival subtree function
assert count_unival_tree(test_tree_single) == 1
assert count_unival_tree(test_tree_two_level_uni) == 3
assert count_unival_tree(test_tree_two_level_dual) == 2
assert count_unival_tree(test_tree_a) == 5
