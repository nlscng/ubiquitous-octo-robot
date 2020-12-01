# A graph is minimally-connected if it is connected and there is no edge that can be removed while still leaving the
# graph connected. For example, any binary tree is minimally-connected.
#
# Given an undirected graph, check if the graph is minimally-connected. You can choose to represent the graph as
# either an adjacency matrix or adjacency list.

"""
A minimally connected graph is basically a tree. I think this is checking if a given graph is a tree.

So a tree with n node has n-1 edge, is full connected and no cycle.
"""

from collections import deque


def is_minimally_connected(graph: {}) -> bool:
    # I am using a single run of DFS for this check, so this should be O(v+e) in time and space
    assert graph

    visited = set()

    walker = list(graph.keys())[0]
    queue = deque([(None, walker)])

    while len(queue) > 0:
        parent, walker = queue.pop()
        if walker not in visited:
            visited.add(walker)

        neighbors = [x for x in graph[walker] if parent is None or x != parent]
        if len([x for x in neighbors if x in visited]) > 0:
            # cycle detected
            return False
        queue.extend(list(zip([walker for _ in range(len(neighbors))], neighbors)))

    return len(visited) == len(graph.keys())


# a - b - d
# |     \
# c       e
t = {
    'a': ['b', 'c'],
    'b': ['a', 'e', 'd'],
    'c': ['a'],
    'd': ['b'],
    'e': ['b']
}

assert is_minimally_connected(t)


# a - b - d
# |     \ |
# c       e
u = {
    'a': ['b', 'c'],
    'b': ['a', 'e', 'd'],
    'c': ['a'],
    'd': ['b', 'e'],
    'e': ['b', 'd']
}
assert not is_minimally_connected(u)

# a - b - d
# |
# c       e
v = {
    'a': ['b', 'c'],
    'b': ['a', 'd'],
    'c': ['a'],
    'd': ['b'],
    'e': []
}
assert not is_minimally_connected(v)

# a   b - d
# |     \
# c       e
w = {
    'a': ['c'],
    'b': ['e', 'd'],
    'c': ['a'],
    'd': ['b'],
    'e': ['b']
}
assert not is_minimally_connected(w)