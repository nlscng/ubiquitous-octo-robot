# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with
# a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s
# could also be considered as a subtree of itself.
from common.treenode.MyBST import StrNode


def is_subtree(s: StrNode, t: StrNode) -> bool:
    # GG: this is naive approach, and O(n * m) time, n and m are size of the trees. There's a linear time solution, which relies
    #  on the fact that a binary tree can be identified by its in-order and (pre or post)-order traversal
    def is_same(a: StrNode, b: StrNode) -> bool:
        # either bfs or dfs, check the tree for identical value and structure:
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False

        return a.val == b.val and is_same(a.left, b.left) and is_same(a.right, b.right)

    visiting = [s]

    while len(visiting) > 0:
        walker = visiting.pop()
        if walker.val == t.val:
            if is_same(walker, t):
                return True
        if walker.left is not None:
            visiting.append(walker.left)
        if walker.right is not None:
            visiting.append(walker.right)

    return False


a = StrNode('a')
b = StrNode('b')
c = StrNode('c')
d = StrNode('d')
e = StrNode('e')

f = StrNode('a')
g = StrNode('b')
h = StrNode('c')

#       g               d
#      f h           b     e
#                  a  c
assert is_subtree(a, a)
d.left = b
b.left = a

g.left = f
#   d     g(b)
#  b     f(a)
# a
assert is_subtree(d, g)
assert is_subtree(d, g)


#    d          g(b)
#  b   e    f(a)   h(c)
# a c
b.right = c
d.right = e
g.right = h
assert is_subtree(d, g)
assert is_subtree(b, g)
