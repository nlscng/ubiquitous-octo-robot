# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# In a directed graph, each node is assigned an uppercase letter. We define a path's value as the number of most
# frequently-occurring letter along that path. For example, if a path in the graph goes through "ABACA", the value of
# the path is 3, since there are 3 occurrences of 'A' on the path.
#
# Given a graph with n nodes and m directed edges, return the largest value path of the graph. If the largest value
# is infinite, then return null.
#
# The graph is represented with a string and an edge list. The i-th character represents the uppercase letter of the
# i-th node. Each tuple in the edge list (i, j) means there is a directed edge from the i-th node to the j-th node.
# Self-edges are possible, as well as multi-edges.
#
# For example, the following input graph:
#
# ABACA
# [(0, 1),
#  (0, 2),
#  (2, 3),
#  (3, 4)]
# Would have maximum value 3 using the path of vertices [0, 2, 3, 4], (A, A, C, A).
#
# The following input graph:
#
# A
# [(0, 0)]
# Should return null, since we have an infinite loop.

def count_most_frequent(arr: list) -> int:
    count = {}
    for one_letter in arr:
        if one_letter not in count:
            count[one_letter] = 1
        else:
            count[one_letter] += 1

    highest_frequency = sorted(count.values())
    return highest_frequency[0]


def largest_value_path(nodes: str, edges: list) -> int:
    walker = init_node = 0
    path_history = {init_node}
    for good_edge in [one_edge for one_edge in edges if one_edge[0] == walker]:
        if good_edge[1] in path_history:
            # detect cycle, and fail out early if so
            return None
        path_history.add(walker[1])


assert largest_value_path("A", [(0, 0)]) == 0
assert largest_value_path("ABACA", [(0, 1), (0, 2), (2, 3), (3, 4)]) == 3
