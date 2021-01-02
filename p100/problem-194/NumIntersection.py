# This problem was asked by Facebook.
#
# Suppose you are given two lists of n points, one list p1, p2, ..., pn on the line y = 0 and the other list q1, q2,
# ..., qn on the line y = 1. Imagine a set of n line segments connecting each point pi to qi. Write an algorithm to
# determine how many pairs of the line segments intersect.

##Facebook

"""
This is interesting. Without noticing some key elements, comparing two list is O(n^2).
Then checking if two pairs of points form an intersection can be done, maybe, in two separate dimension?
As in, if they overlaps in X axis and Y axis, they should intersect?

I think that's true, on an intuition level.
"""

from typing import List

Segment = (int, int)
Point = (int, int)


def intersect_one_dimension(a: Segment, b: Segment) -> bool:
    # GG: this logics of checking for overlapping is quite common I think.
    low_a, low_b = min(a[0], a[1]), min(b[0], b[1])
    high_a, high_b = max(a[0], a[1]), max(b[0], b[1])
    return max(low_a, low_b) <= min(high_a, high_b)


assert intersect_one_dimension((3, 6), (4, 9))
assert intersect_one_dimension((1, 9), (4, 5))
assert not intersect_one_dimension((1, 3), (5, 8))


def intersect_two_dimension(a: Point, b: Point) -> bool:
    a_x = (a[0][0], a[1][0])
    a_y = (a[0][1], a[1][1])
    b_x = (b[0][0], b[1][0])
    b_y = (b[0][1], b[1][1])
    return intersect_one_dimension(a_x, b_x) and intersect_one_dimension(a_y, b_y)


assert intersect_two_dimension(((0, 0), (2, 2)), ((0, 2), (2, 0)))
assert not intersect_two_dimension(((0, 0), (2, 0)), ((0, 2), (2, 2)))

"""
1,   4,   8

 2, 3,  6

"""


def num_intersections(lis_a: List[int], lis_b: List[int]) -> int:
    assert lis_a and lis_a and len(lis_a) == len(lis_b)
    segments = []
    for i in range(len(lis_a)):
        segments.append((lis_a[i], lis_b[i]))

    count = 0
    N = len(segments)
    for i in range(N):
        for j in range(i + 1, N):
            a = segments[i]
            b = segments[j]
            if a[0] != b[0] and a[1] != b[1] and intersect_one_dimension(a, b) \
                    and ((a[0] > b[0] and a[1] < b[1]) or (a[0] < b[0] and a[1] > b[1])):
                count += 1

    return count


assert num_intersections([1, 4, 9], [2, 3, 6]) == 0
assert num_intersections([1, 2, 3], [2, 3, 4]) == 0
assert num_intersections([1, 4, 5], [4, 2, 3]) == 2
