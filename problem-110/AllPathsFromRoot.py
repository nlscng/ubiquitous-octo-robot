# This problem was asked by Facebook.
#
# Given a binary tree, return all paths from the root to leaves.
#
# For example, given the tree:
#
#    1
#   / \
#  2   3
#     / \
#    4   5
# Return [[1, 2], [1, 3, 4], [1, 3, 5]].


'''

modified dfs might be a start, and it's O(n) in time and O(h) in space, n is num of nodes in tree, h is height of three


'''

from common.treenode.MyBST import BstIntNode


def find_all_paths(root: BstIntNode) -> []:
    if not root:
        return []

    walker = root
    stack = [walker]
    all_paths = []
    cur_path = []
    visited = set()

    while len(stack) > 0:
        walker = stack.pop()
        cur_path.append(walker)

        if walker.left is None and walker.right is None:
            # we found a leaf, record a path and backtrack up
            one_path = [x.val for x in cur_path]
            all_paths.append(one_path)
            tail = cur_path.pop()
            visited.add(tail)

            # GG: this is the tricky part about this modded DFS, back track to where necessary; this is same as graph
            #  dfs finding all path I think
            tail = cur_path[-1]
            while len(cur_path) > 1 and (tail.left is None or tail.left in visited) and \
                    (tail.right is None or tail.right in visited):
                cur_path.pop()
                tail = cur_path[-1]

        else:
            # not we append right child before left, so we pop left child first on stack
            if walker.right is not None:
                stack.append(walker.right)
            if walker.left is not None:
                stack.append(walker.left)

    return all_paths


a = BstIntNode(1)
b = BstIntNode(2)
c = BstIntNode(3)
d = BstIntNode(4)
e = BstIntNode(5)
a.left = b
a.right = c
c.left = d
c.right = e

assert find_all_paths(a) == [[1, 2], [1, 3, 4], [1, 3, 5]], "Actual: {}".format(find_all_paths(a))

a.left = b
a.right = c
b.left = d
b.right = e
c.left = None
c.right = None
assert find_all_paths(a) == [[1, 2, 4], [1, 2, 5], [1, 3]], "Actual: {}".format(find_all_paths(a))
