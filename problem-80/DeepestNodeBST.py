# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.
#
#     a
#    / \
#   b   c
#  /
# d

from common.treenode.MyBST import MyBstNodeStringVal


def deepest_node(root: MyBstNodeStringVal) -> int:
    # run bfs or dfs and track all the nodes with their depth,
    # return from the result a node with max depth
    # for dfs, O(n) in time, and O(n) in space
    # if I do bfs, O(n) in time, O(1) in space, just have to track the last node explored, and once
    # the queue is empty, return said node, since it's guaranteed to be at the deepest level

    depth_memo = {}  # a dict of int -> list of nodes, depth and nodes with that depth

    visited = [(0, root)]
    while len(visited) != 0:
        walker_depth, walker = visited.pop()
        if walker_depth not in depth_memo:
            depth_memo[walker_depth] = []
        depth_memo[walker_depth].append(walker)
        if walker.left is not None:
            visited.append((walker_depth + 1, walker.left))
        if walker.right is not None:
            visited.append((walker_depth + 1, walker.right))

    return depth_memo[max(depth_memo.keys())][0]


a = MyBstNodeStringVal('a')
b = MyBstNodeStringVal('b')
c = MyBstNodeStringVal('c')
d = MyBstNodeStringVal('d')

assert deepest_node(a) == a

a.left = b
assert deepest_node(a) == b

a.right = c
b.left = d
assert deepest_node(a) == d
