# This problem was asked by Facebook.
#
# Suppose you are given two lists of n points, one list p1, p2, ..., pn on the line y = 0 and the other list q1, q2,
# ..., qn on the line y = 1. Imagine a set of n line segments connecting each point pi to qi. Write an algorithm to
# determine how many pairs of the line segments intersect.

##Facebook
##TBC
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
    # GG: this logics of checking for overlapping or intersection is quite common I think.
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


def num_intersection(lis_a: List[Point], lis_b: List[Point]) -> int:
    assert lis_a and lis_b
    count = 0
    for a in lis_a:
        for b in lis_b:
            if intersect_two_dimension(a, b):
                count += 1

    return count


assert num_intersection()