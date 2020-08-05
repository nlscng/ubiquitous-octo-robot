#     6
#    / \
#   3   4
#  /   / \
# 5   1   8
#  \
#   2
#  / \
# 9   7
#
# Given a binary tree, return a list of its node in column first then depth first fashion
# that is, this above tree should return [5, 9, 3, 2, 6, 1, 7, 4, 8], 5 adn 9 being the same
# column, 3 and 2 the same, 6, 1 and 7  the same column

from common.treenode.MyBST import IntNode


def col_print_tree(root: IntNode) -> list:
    # bfs the tree nodes to get a processed info for each column and its node
    # bfs will maintain depth first, aka deeper nodes will come after.

    queue = [(root, 0)] # the queue will hold tuples of node and its col, col is relative to root
    walker = None
    dict = {}

    # keep records of left most and right most col, this will save us from having to sort
    # dict by keys later
    min_col, max_col = 0, 0

    while len(queue) > 0:
        walker = queue.pop()
        node, col = walker
        # add to dict
        if col not in dict:
            dict[col] = [node.val]
        else:
            dict[col].append(node.val)
        # update min and max col
        min_col = min(min_col, col)
        max_col = max(max_col, col)
        # navigate down the tree
        if node.left is not None:
            queue.append((node.left, col - 1))
        if node.right is not None:
            queue.append((node.right, col + 1))

    res = []
    # print from the dictionary
    for key in range(min_col, max_col + 1):
        res += dict[key]

    return res


a = IntNode(6)
b = IntNode(3)
c = IntNode(4)
d = IntNode(5)
e = IntNode(1)
f = IntNode(8)
g = IntNode(2)
h = IntNode(9)
i = IntNode(7)
a.left = b
a.right = c
b.left = d
d.right = g
g.left = h
g.right = i
c.left = e
c.right = f
assert col_print_tree(a) == [5, 9, 3, 2, 6, 1, 7, 4, 8]

