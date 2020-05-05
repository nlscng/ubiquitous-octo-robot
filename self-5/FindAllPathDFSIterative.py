import copy


def find_all_path_to_node_dfs(vertices: list, edges: list, src: int, dst: int):
    walker = src
    explore_stack = [walker]
    path_stack = []
    found_paths = []
    visited = [False] * len(vertices)  # an list of bool is better than a set, we need quick access/removal later
    while len(explore_stack) > 0:
        walker = explore_stack.pop()
        visited.add(walker)
        path_stack.append(walker)

        if walker == dst:
            found_paths.append(path_stack)
        else:
            neighbors = [tgt for src, tgt in edges if src == walker and tgt not in visited]
            for one_neighbor in neighbors:
                explore_stack.append(one_neighbor)

    pass


# SEE: https://gist.github.com/basp1/c3a097c3e8988eda78999dd4ccb5a101
def foo(vertices: list, edges: list, src: int, dst: int) -> list:
    explored_stack = [src]
    explored_parent_stack = [src]
    path = []  # it's actually java linked hashset, using a list here so we'll take the penalty
    found_paths = []

    while len(explored_stack) > 0:
        walker = explored_stack.pop()
        level = explored_parent_stack.pop()

        while len(path) > 0 and path[-1] != level:
            path.pop()

        path.append(walker)
        has_new_node_path = False
        neighbors = [tgt for src, tgt in edges if src == walker]
        for one_neighbor in neighbors:
            if one_neighbor in path:
                continue

            if dst == one_neighbor:
                found = copy.deepcopy(path)
                found.append(dst)
                found_paths.append(found)
                continue
            else:
                has_new_node_path = True
                explored_stack.append(one_neighbor)
                explored_parent_stack.append(walker)

        if not has_new_node_path:
            path.pop()

    return found_paths


vertices_1 = [0, 1, 2, 3]
edges_1 = [(0, 1), (0, 2), (1, 3), (2, 1), (2, 3)]
# assert dfs_recursive(t_vertice_1, t_graph_1, 'D') is not None
print(foo(vertices_1, edges_1, 0, 3))

vertices_2 = [0,1,2]
edges_2 = [(0,1), (1,2), (2,0)]
print(foo(vertices_2, edges_2, 0, 2))
