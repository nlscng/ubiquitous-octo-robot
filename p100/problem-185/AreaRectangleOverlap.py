# Given two rectangles on a 2D graph, return the area of their intersection. If the rectangles don't intersect, return 0.
#
# For example, given the following rectangles:
#
# {
#     "top_left": (1, 4),
#     "dimensions": (3, 3) # width, height
# }
# and
#
# {
#     "top_left": (0, 5),
#     "dimensions": (4, 3) # width, height
# }
# return 6.


"""
I think this can be reduce into two separate line overlap problem, and take the product of those two
"""
from typing import Tuple


def line_segment_overlap(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    assert a and b
    lower_bound = max(a[0], b[0])
    upper_bound = min(a[1], b[1])
    return 0 if lower_bound >= upper_bound else upper_bound - lower_bound


assert line_segment_overlap((0, 3), (2, 6)) == 1
assert line_segment_overlap((0, 2), (3, 6)) == 0


class Square:
    def __init__(self, top_left: Tuple[int, int], width: int, height: int):
        self.top_left_x = top_left[0]
        self.top_left_y = top_left[1]
        self.width = width
        self.height = height


def rectangle_area_overlap(s: Square, t: Square) -> int:
    assert s and t

    width = line_segment_overlap((s.top_left_x, s.top_left_x + s.width), (t.top_left_x, t.top_left_x + t.width))
    height = line_segment_overlap((s.top_left_y, s.top_left_y + s.height), (t.top_left_y, t.top_left_y + t.height))

    return width * height


t1 = Square((1, 4), 3, 3)
t2 = Square((0, 5), 4, 3)
assert rectangle_area_overlap(t1, t2) == 6
