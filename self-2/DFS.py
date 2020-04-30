import copy


def dfs_recursive_all_path(v_values: list, graph: list, k: chr) -> list:
    """
    Given a directed graph, in 2D adjancency array format, return a valid path to a vertex containing target value of k
    from a depth first search.
    :param: v_values: a list of vertex values in characters, in this self-made implementation
    :param graph: a 2D array for a graph in adjacency matrix format
    :param k: the target value for the search
    :return: a valid path to a vertex containing value k, none otherwise
    """
    if not isinstance(graph, list) or not isinstance(graph[0], list):
        raise Exception('Expected a 2D array for graph in adjacency matrix format.')

    if not isinstance(v_values, list) or not v_values:
        raise Exception('Expected a list containing values for each of the vertex in graph.')

    if len(v_values) != len(graph):
        raise Exception('Size of unmatched.')

    num_v = len(v_values)
    visited = [False] * num_v
    found_paths = []
    explore_recur(0, v_values, visited, graph, k, [], found_paths)
    return found_paths


def explore_recur(v: int, v_values: list, visited: list, graph: list, k: chr, path: list, found_paths: list):
    my_visited = copy.deepcopy(visited)
    my_visited[v] = True
    my_path = copy.deepcopy(path)
    my_path.append(v)
    if v_values[v] == k:
        found_paths.append(my_path)
    neighbors: list = [v_idx for v_idx, one_v in enumerate(graph[v]) if not visited[v_idx] and one_v]
    for one_neighbor in neighbors:
        explore_recur(one_neighbor, v_values, my_visited, graph, k, my_path, found_paths)


t_vertice_1 = ['A', 'B', 'C', 'D']
t_graph_1 = [[False, True, True, False],
             [False, False, False, True],
             [False, True, False, True],
             [False, False, False, False]]
# assert dfs_recursive(t_vertice_1, t_graph_1, 'D') is not None
print(dfs_recursive_all_path(t_vertice_1, t_graph_1, 'D'))