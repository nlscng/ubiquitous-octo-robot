# This problem was asked by Google.
#
# You are given given a list of rectangles represented by min and max x- and y-coordinates. Compute whether or not a
# pair of rectangles overlap each other. If one rectangle completely covers another, it is considered overlapping.
#
# For example, given the following rectangles:
#
# {
#     "top_left": (1, 4),
#     "dimensions": (3, 3) # width, height
# },
# {
#     "top_left": (-1, 3),
#     "dimensions": (2, 1)
# },
# {
#     "top_left": (0, 5),
#     "dimensions": (4, 3)
# }
# return true as the first and third rectangle overlap each other.

##Google
from typing import List


class Rectangle:
    def __init__(self, top_left_x: int, top_left_y: int, width: int, height: int):
        assert width and height
        self.top_left_x = top_left_x
        self.top_left_y = top_left_y
        self.width = width
        self.height = height

    def info(self):
        return self.top_left_x, self.top_left_x + self.width, self.top_left_y, self.top_left_y - self.height


def complete_covers(rec_a: Rectangle, rec_b: Rectangle) -> bool:
    ax_low, ax_high, ay_low, ay_high = rec_a.info()
    bx_low, bx_high, by_low, by_high = rec_b.info()

    covers_x_axis = ((ax_low <= bx_low) and (ax_high >= bx_high)) or ((ax_low >= bx_low) and (ax_high <= bx_high))
    covers_y_axis = ((ay_low <= by_low) and (ay_high >= by_high)) or ((ay_low >= by_low) and (ay_high <= by_high))
    return covers_y_axis and covers_x_axis


def rectangles_complete_cover(lis: List[Rectangle]) -> bool:
    assert lis
    N = len(lis)
    for i in range(N):
        for j in range(i + 1, N):
            if complete_covers(lis[i], lis[j]):
                return True
    return False


test_a = Rectangle(1, 4, 3, 3)
test_b = Rectangle(-1, 3, 2, 1)
test_c = Rectangle(0, 5, 4, 3)
assert rectangles_complete_cover([test_a, test_b, test_a])
