# Given a n-ary tree of positive and negative int, prune away nodes whose subtree sum up to zero
"""
       7
    4    9
  / | \
 -1 0 -1
 /
-2
"""


class Node:
    def __init__(self, value: int, children=[]):
        self.value = value
        self.children = children


def prune(root: Node) -> Node:
    if root is None:
        return root

    def help(node: Node) -> int:
        if len(node.children) == 0:
            return node.value

        children_sum = 0
        idx = 0
        while idx < len(node.children):
            one_child_sum = help(node.children[idx])
            if one_child_sum == 0:
                # GG: I made this mistake here, removing element as you spin through it is tricky
                node.children.pop(idx)
                idx -= 1

            children_sum += one_child_sum
            idx += 1

        return children_sum + node.value

    help(root)
    return root


a = Node(-2)
b = Node(-1, [a])
c = Node(0)
d = Node(-1)
e = Node(4, [b, c, d])
f = Node(9)
g = Node(7, [e, f])

print(prune(g))
