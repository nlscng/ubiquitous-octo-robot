# This problem was asked by Facebook.
#
# Given a binary tree, return the level of the tree with minimum sum.

"""
     3
  4      2
-3 1  -5  2

BFS through the tree, I will have to modified it somewhow for sure to know which level this node is. At the same
time keep a current max_sum, update it as we go along the levels

"""

from common.treenode.MyBST import IntNode


def max_level_sum(root: IntNode) -> int:
    # this is O(n) in time and O(n) in space, n is number of nodes in bst
    if not root:
        return 0

    cur_max_sum = 0
    cur_sum = 0
    cur_level = 0
    queue = [(root, cur_level)]

    while len(queue) > 0:
        node, depth = queue.pop(0)
        if node.left is not None:
            queue.append((node.left, depth + 1))
        if node.right is not None:
            queue.append((node.right, depth + 1))

        if cur_level == depth:
            cur_sum += node.val
        else:
            cur_max_sum = max(cur_max_sum, cur_sum)
            cur_level = depth
            cur_sum = node.val

    cur_max_sum = max(cur_max_sum, cur_sum)

    return cur_max_sum


#      3
#   4      2
# -3 1  -5  2
a = IntNode(3)
b = IntNode(4)
c = IntNode(2)
d = IntNode(-3)
e = IntNode(1)
f = IntNode(-5)
g = IntNode(2)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

assert max_level_sum(a) == 6
