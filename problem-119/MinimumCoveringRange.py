# This problem was asked by Google.
#
# Given a set of closed intervals, find the smallest set of numbers that covers all the intervals. If there are
# multiple smallest sets, return any of them.
#
# For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of numbers that covers all these intervals
# is {3, 6}.

"""

[0, 3], [2, 6], [3, 4], [6, 9]

0...3
   2....6
    3.4
        6....9

It seems like the minimum covering range would have a start of min of all ending time, and an end of max of all
starting time

"""


def minimum_covering_range(intervals: list) -> []:
    if not intervals:
        return []
    if len(intervals) == 1:
        return intervals

    return [min([end for start, end in intervals]), max([start for start, end in intervals])]


assert minimum_covering_range([[0, 1], [1, 2], [3, 4]]) == [1, 3]
assert minimum_covering_range([[0, 3], [2, 6], [3, 4], [6, 9]]) == [3, 6]
