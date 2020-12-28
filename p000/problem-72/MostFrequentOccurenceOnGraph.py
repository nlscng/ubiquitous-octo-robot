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

##Google
##Review

def count_most_frequent(path: list, nodes: str) -> int:
    count = {}
    for one_stop in path:
        key = nodes[one_stop]
        if key not in count:
            count[key] = 1
        else:
            count[key] += 1
    highest_frequency = sorted(count.values(), reverse=True)
    return highest_frequency[0]


def largest_value_path(nodes: str, edges: list) -> int:
    cur_max = [0]
    found_loop = [False]

    def explore_recur(walker: int, path: list):
        if found_loop[0]:
            return True
        cur_count = count_most_frequent(path, nodes)
        cur_max[0] = max(cur_count, cur_max[0])

        for src, tgt in [one_edge for one_edge in edges if one_edge[0] == walker]:
            if tgt in path:
                # detected cycle, and fail out early if so
                found_loop[0] = True
                break
            path.append(tgt)
            explore_recur(tgt, path)
            path.pop()  # backtrack

    for i in range(len(nodes)):
        explore_recur(i, [i])
        if found_loop[0]:
            return None

    return cur_max[0]


# assert count_most_frequent([0,2,3,4], 'ABACA') == 3

assert largest_value_path("A", [(0, 0)]) is None, "Actual :{}".format(largest_value_path("A", [(0, 0)]))
res = largest_value_path("ABACA", [(0, 1), (0, 2), (2, 3), (3, 4)])
assert res == 3, "Actual: {}".format(res)
