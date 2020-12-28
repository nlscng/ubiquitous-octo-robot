# This problem was asked by Google.
#
# You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall.
# Each False boolean represents a tile you can walk on.
#
# Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach
# the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down,
# and right. You cannot move through walls. You cannot wrap around the edges of the board.
#
# For example, given the following board:
#
# [[f, f, f, f],
# [t, t, f, t],
# [f, f, f, f],
# [f, f, f, f]]
#
# and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end
# is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.

##Google
##Review

from collections import deque


def find_path_in_matrix(dungeon, src, snk):
    def in_range(loc):
        # closure to include the dungeon map
        left_bound, right_bound = 0, len(dungeon[0]) - 1
        low_bound, up_bound = 0, len(dungeon) - 1
        return low_bound <= loc[0] <= up_bound and left_bound <= loc[1] <= right_bound

    def is_walkable(loc):
        # closure to include the dungeon map
        x, y = loc
        return dungeon[x][y] == 'f'

    def new_neighbors(loc):
        # closure to include the "been there" set
        # x being the vert axis and y is the horizontal axis in this dungeon
        x, y = loc[0], loc[1]
        north = (x - 1, y)
        south = (x + 1, y)
        east = (x, y + 1)
        west = (x, y - 1)
        return [neighbor for neighbor in [north, south, east, west] if
                in_range(neighbor) and
                neighbor not in been_there and
                is_walkable(neighbor)]

    if not dungeon or not src or not snk:
        return None
    elif not in_range(src) or not in_range(snk):
        return None
    elif not is_walkable(src) or not is_walkable(snk):
        return None

    been_there = set()

    path_q = deque()
    path_q.append((src, 0))

    walker = None
    while len(path_q) > 0:
        walker = path_q.popleft()
        loc, level = walker
        if loc == snk:
            return level
        neighbors = new_neighbors(loc)
        path_q.extend([(one_neighbor, level + 1) for one_neighbor in neighbors])

    return None


matrix = [["f", "f", "f", "f"],
          ["t", "t", "f", "t"],
          ["f", "f", "f", "f"],
          ["f", "f", "f", "f"]]

assert find_path_in_matrix(matrix, (0, 0), (0, 0)) == 0, "actual: {}".format(
    find_path_in_matrix(matrix, (0, 0), (0, 0)))
assert find_path_in_matrix(matrix, (1, 0), (0, 0)) is None, "actual: {}".format(
    find_path_in_matrix(matrix, (1, 0), (0, 0)))
assert find_path_in_matrix(matrix, (3, 0), (0, 0)) == 7, "actual: {}".format(
    find_path_in_matrix(matrix, (3, 0), (0, 0)))
assert find_path_in_matrix(matrix, (3, 0), (0, 3)) == 6, "actual: {}".format(
    find_path_in_matrix(matrix, (3, 0), (0, 3)))

matrix = [["f", "f", "f", "f"],
          ["t", "t", "t", "f"],
          ["f", "f", "f", "f"],
          ["f", "f", "f", "f"]]

assert find_path_in_matrix(matrix, (0, 0), (0, 0)) == 0
assert find_path_in_matrix(matrix, (3, 0), (0, 0)) == 9
assert find_path_in_matrix(matrix, (2, 0), (3, 3)) == 4
