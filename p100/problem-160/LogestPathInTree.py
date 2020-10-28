# This problem was asked by Uber.
#
# Given a tree where each edge has a weight, compute the length of the longest path in the tree.
#
# For example, given the following tree:
#
# a /|\ b c d / \ e   f / \ g   h and the weights: a-b: 3, a-c: 5, a-d: 8, d-e: 2, d-f: 4, e-g: 1, e-h: 1,
# the longest path would be c -> a -> d -> f, with a length of 17.
#
# The path does not have to pass through the root, and each node can have any amount of children.

"""
This would be easier if definition of path is going from the root.

Any paths means I can go from leaf to leaf. And this is not a binary tree, any node can have any number of children.


"""


class AdjacencyListNode:
    def __init__(self, from_node_name: str, to_node_name: str, weight: int):
        assert weight > 0 and from_node_name and to_node_name
        self.fn = from_node_name
        self.tn = to_node_name
        self.w = weight


def max_sum_path(lis: list) -> int:
    assert list and isinstance(lis[0], AdjacencyListNode)
    # I assume root is passed in s the first element of the adj matrix

    cur_max = [0]

    def get_max_from_children(node: str) -> int:
        children = [[x.tn, x.w] for x in lis if node == x.fn]
        if len(children) == 0:
            return 0
        else:
            children_paths_sum = [get_max_from_children(x[0]) + x[1] for x in children]
            children_paths_sum.sort()
            top_two_sum = sum(children_paths_sum[-2:])
            cur_max[0] = max(cur_max[0], top_two_sum)
            return children_paths_sum[-1]

    get_max_from_children(lis[0].fn)
    return cur_max[0]


tree = [
    AdjacencyListNode('a', 'b', 3),
    AdjacencyListNode('a', 'c', 5),
    AdjacencyListNode('a', 'd', 8),
    AdjacencyListNode('d', 'e', 2),
    AdjacencyListNode('d', 'f', 4),
    AdjacencyListNode('e', 'g', 1),
    AdjacencyListNode('e', 'h', 1)
]

print(max_sum_path(tree))
assert max_sum_path(tree) == 17
