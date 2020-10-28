# This problem was asked by Google.
#
# You are in an infinite 2D grid where you can move in any of the 8 directions:
#
# (x,y) to (x+1, y), (x - 1, y), (x, y+1), (x, y-1), (x-1, y-1), (x+1,y+1), (x-1,y+1), (x+1,y-1) You are given a
# sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which
# you can achieve it. You start from the first point.
#
# Example:
#
# Input: [(0, 0), (1, 1), (1, 2)]
# Output: 2
# It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).


'''

since the order of the points to be covered is given, there's no dfs or bfs or any type of search
we are only counting the distance between points, and turn those into num steps

'''


def num_steps(path: list) -> int:
    if len(path) < 2:
        return len(path)

    res = 0
    prev = path[0]
    for one_cord in path[1:]:
        step = max(abs(prev[0] - one_cord[0]), abs(prev[1] - one_cord[1]))
        res += step
        prev = one_cord

    return res


assert num_steps([(0, 0), (1, 1), (1, 2)]) == 2
assert num_steps([(0, 0), (1, 2), (4, -3)]) == 7
