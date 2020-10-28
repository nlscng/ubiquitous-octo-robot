# Given a list of points, a central point, and an integer k, find the nearest k points from the central point.
#
# For example, given the list of points [(0, 0), (5, 4), (3, 1)], the central point (1, 2), and k = 2, return [(0,
# 0), (3, 1)].

"""
This should be relatively straight forward. Since distance is sqrt of sum, we can skip the sqrt calculation and still
have the distances be in the same order within the given points.

So basically we are sorting these points by sum of their x-delta to center point, and y-delta to center point,
then returning the first k of them
"""


def k_nearest_neighbor(lis: list, k: int, center: list) -> list:
    ds = lis.copy()
    ds.sort(key=lambda p: ((p[0] - center[0]) ^ 2) + ((p[1] - center[1]) ^ 2), reverse=False)
    return ds[:k]


assert k_nearest_neighbor([[3, 3], [5, -1], [-2, 4]], 2, [0, 0]) == [[3, 3], [-2, 4]]
assert k_nearest_neighbor([[0, 0], [5, 4], [3, 1]], 2, [1, 2]) == [[0, 0], [3, 1]]