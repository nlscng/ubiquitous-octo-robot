#
# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given an undirected graph represented as an adjacency matrix and an integer k, write a function to determine
# whether each vertex in the graph can be colored such that no two adjacent vertices share the same color using at
# most k colors.

UNCOLORED = -1


# SEE: AI textbook 3rd. Ed. Ch6, p219 backtracking search
def is_neighbor_wise_legal(node: int, color: int, cur_assignment: {}, graph: list):
    neighbors = [idx for idx, is_connected in enumerate(graph[node]) if
                 idx != node and is_connected and cur_assignment[idx] != UNCOLORED]
    neighbor_colors = [cur_assignment[one_neighbor] for one_neighbor in neighbors]
    return color not in neighbor_colors


def is_assignment_complete(cur_assignment: {}, graph: []):
    n_keys = len(cur_assignment)
    if any(one_value == UNCOLORED for one_value in cur_assignment.values()):
        return False

    for i in range(n_keys):
        neighbors = [idx for idx, is_connected in enumerate(graph[i]) if idx > i and is_connected]
        for one_neighbor in neighbors:
            if cur_assignment[i] == cur_assignment[one_neighbor]:
                return False
    return True


def select_uncolored_node(graph: {}) -> int:
    # This is where we can implement 'least constraining values' or 'most constrained variable' for next coloring node
    for one_key in graph:
        if graph[one_key] == UNCOLORED:
            return one_key
    return None


def legal_color_for_node(cur_assignment: {}, node: int, graph: list, k: int) -> list:
    neighbors = [idx for idx, is_connected in enumerate(graph[node]) if
                 idx != node and is_connected and cur_assignment[idx] != UNCOLORED]
    used_colors = [cur_assignment[one_neighbor] for one_neighbor in neighbors]
    legal_colors = [n for n in range(k) if n not in used_colors]
    return legal_colors


def backtrack_search(cur_assignment: {}, graph: list, k: int):
    if is_assignment_complete(cur_assignment, graph):
        return True

    next_node = select_uncolored_node(cur_assignment)
    if next_node is None:
        raise Exception("Assignment isn't completed yet but we failed to find a next node to color")

    legal_colors = legal_color_for_node(cur_assignment, next_node, graph, k)
    for one_color in legal_colors:
        if is_neighbor_wise_legal(next_node, one_color, cur_assignment, graph):
            cur_assignment[next_node] = one_color
            result = backtrack_search(cur_assignment, graph, k)
            if result:
                return result
        # one_color failed to achieve complete assignment, move on and try next legal color
        cur_assignment[next_node] = UNCOLORED

    return None


def is_k_colorable(graph, k: int):
    if not isinstance(graph, list) or not isinstance(graph[0], list):
        raise Exception("Expected a 2D list for adjacency map, but graph isn't of type list")
    init_assignment = {node_idx: UNCOLORED for node_idx in range(len(graph[0]))}
    return backtrack_search(init_assignment, graph, k) is not None


assert is_k_colorable([[0]], 1)
two_by_two = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0]
]

assert is_k_colorable(two_by_two, 2)
assert not is_k_colorable(two_by_two, 1)

triangle = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]
assert not is_k_colorable(triangle, 1)
assert not is_k_colorable(triangle, 2)
assert is_k_colorable(triangle, 3)

two_by_two_net = [
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0],
]
assert is_k_colorable(two_by_two_net, 4)
assert not is_k_colorable(two_by_two_net, 3)