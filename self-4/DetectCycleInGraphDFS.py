def detect_cycle(vertices: list, edges: list) -> bool:
    # iterative DFS down the graph and note pre and post order number for each vertices
    # any back edges would indicate a cycle, and back edges have increasing post order number from src to target

    walker = vertices[0]
    post_orders = {x: 0 for x in vertices}
    explore_stack: list = [walker]
    path_stack = []
    visited = set()
    clock = 0
    while len(explore_stack) > 0:
        walker = explore_stack.pop()
        if walker not in visited:
            path_stack.append(walker)  # add to the current active path stack
            visited.add(walker)
            neighbors = [target for src, target in edges if src == walker and target not in visited]
            # TODO: think about how to detect self loop
            if not neighbors:
                done_v = path_stack.pop()
                post_orders[done_v] = clock
                clock += 1
            else:
                for one_neighbor in neighbors:
                    explore_stack.append(one_neighbor)

    # clean up path stack, if there are vertices left when we are done exploring
    while len(path_stack) > 0:
        walker = path_stack.pop()
        post_orders[walker] = clock
        clock += 1

    print(post_orders)

    return False


t_vertices = [0, 1, 2, 3]
t_edges = [(0, 1),
           (0, 2),
           (1, 3),
           (2, 1),
           (2, 3)]

assert detect_cycle(t_vertices, t_edges)
