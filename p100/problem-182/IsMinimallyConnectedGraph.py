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


def is_minimally_connected(graph: list) -> bool:
    assert graph

    visited = set()
    num_nodes = 0
    num_edges = 0

    walker = graph[0][0]
    queue = deque([walker])

    while len(queue) > 0:
        walker = queue.popleft()
        if walker not in visited:
            visited.add(walker)

        #TBC

    pass



