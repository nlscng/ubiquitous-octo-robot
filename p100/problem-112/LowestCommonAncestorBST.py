# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Twitter.
#
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree. Assume that each node in
# the tree also has a pointer to its parent.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w
# as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

from common.treenode.MyBST import IntNode

def lowest_common_ancestor(root: IntNode, node_a: IntNode, node_b: IntNode) -> IntNode:
    # this is O(h) in time, and O(1) in space; h is height of the tree
    def get_parents(node: IntNode) -> list:
        parents = [node]
        walker = node
        while walker.parent is not None:
            walker = walker.parent
            parents.append(walker)
        return parents

    parents_a = get_parents(node_a)
    parents_b = get_parents(node_b)

    len_a, len_b = len(parents_a), len(parents_b)
    delta = len_a - len_b

    if delta > 0:
        parents_a = parents_a[delta:]
    else:
        parents_b = parents_b[-delta:]

    assert len(parents_b) == len(parents_a)

    for idx in range(len(parents_a)):
        if parents_a[idx] == parents_b[idx]:
            return parents_a[idx]

    return None


a = IntNode(1)
b = IntNode(2)
c = IntNode(3)
d = IntNode(4)
e = IntNode(5)
f = IntNode(6)
g = IntNode(7)
h = IntNode(8)
i = IntNode(9)

a.left = b
b.parent = a
a.right = c
c.parent = a
b.left = d
d.parent = b
b.right = e
e.parent = b
c.left = f
f.parent = c
c.right = g
g.parent = c
f.left = h
h.parent = f
f.right = i
i.parent = f

#      a
#   b     c
#  d  e  f g
#       h i
assert lowest_common_ancestor(a, a, a) == a
assert lowest_common_ancestor(a, b, c) == a
assert lowest_common_ancestor(a, e, b) == b
assert lowest_common_ancestor(a, e, h) == a
assert lowest_common_ancestor(a, g, i) == c

