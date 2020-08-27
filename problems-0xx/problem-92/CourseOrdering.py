# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Airbnb.
#
# We're given a hashmap associating each courseId key with a list of courseIds values, which represents that the
# prerequisites of courseId are courseIds. Return a sorted ordering of courses such that we can finish all courses.
#
# Return null if there is no such ordering.
#
# For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}, should return ['CSC100',
# 'CSC200', 'CSCS300'].

from common.treenode.MyBST import StrNode


def order_recur(catalog: {}) -> list:
    # turn the catalog into list of nodes and its edges
    nodes, edges = get_nodes_and_edges(catalog)
    post_order = {k: -1 for k in nodes}
    visited = set()
    clock = [0]

    def dfs_recur(node):
        if node not in visited:
            visited.add(node)
            neighbors = [tgt for src, tgt in edges if src == node and tgt not in visited]
            for one_neighbor in neighbors:
                dfs_recur(one_neighbor)
            post_order[node] = clock[0]
            clock[0] += 1

    likely_src = get_likely_src(catalog)
    dfs_recur(likely_src)

    ordered = [0] * len(nodes)
    for k, v in post_order.items():
        ordered[v] = k

    return ordered[::-1]


def get_nodes_and_edges(dict: {}) -> ():
    # turn the catalog into list of nodes and its edges
    nodes = []
    edges = []
    for key, values in dict.items():
        nodes.append(key)
        for one_source in values:
            edges.append([one_source, key])
    return nodes, edges


def get_likely_src(catalog):
    return [k for k, v in sorted(catalog.items(), key=lambda one_item: len(one_item), reverse=True)][0]


a = {'a': [], 'c': ['a', 'b'], 'b': ['a']}
assert order_recur(a) == ['a', 'b', 'c']

b = {'a': [], 'b': ['a'], 'c': ['a', 'b'], 'd': ['b', 'c']}
assert order_recur(b) == ['a', 'b', 'c', 'd']
