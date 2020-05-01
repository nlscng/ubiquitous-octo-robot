def dfs_iter(v_values: list, graph: list, k: chr, src: int = None) -> bool:
    """
    Given a graph in adjacency matrix, a list of vertices values, determine if a target value k found and reachable from
    source, or the first vertex given in graph if soruce is not provided. This should be more or less textbook DFS
    implementation.
    :param v_values:
    :param graph:
    :param k:
    :return:
    """
    start = src if src is not None else 0
    visited = [False] * len(v_values)
    stack = []
    stack.append(start)

    while len(stack) > 0:
        walker = stack.pop()
        visited[walker] = True
        if v_values[walker] == k:
            return True
        neighbors = [idx for idx, has_edge in enumerate(graph[walker]) if has_edge and not visited[idx]]
        for one_neighbor in neighbors:
            stack.append(one_neighbor)

    return False


graph_1 = [[False, True, True, False],
           [False, False, False, True],
           [False, True, False, True],
           [False, False, False, False]]
v_values_1 = ['A', 'B', 'C', 'D']

assert dfs_iter(v_values_1, graph_1, 'D')
assert not dfs_iter(v_values_1, graph_1, 'A', 3)

