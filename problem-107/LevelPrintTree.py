# This problem was asked by Microsoft.
#
# Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.
#
#   1
#  / \
# 2   3
#    / \
#   4   5


'''
First thing I think of is bfs.


'''

from common.treenode.MyBST import IntNode


def level_print_tree(node: IntNode) -> list:
    if not node:
        return []

    walker = node
    queue = [walker]
    res = []

    while len(queue) > 0:
        head = queue.pop(0)
        res.append(head.val)
        if head.left is not None:
            queue.append(head.left)
        if head.right is not None:
            queue.append(head.right)

    return res


a = IntNode(1)
b = IntNode(2)
c = IntNode(3)
d = IntNode(4)
e = IntNode(5)
a.left = b
a.right = c
c.left = d
c.right = e

assert level_print_tree(a) == [1, 2, 3, 4, 5], "Actual: {}".format(level_print_tree(a))
