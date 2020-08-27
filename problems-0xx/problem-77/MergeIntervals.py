# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Snapchat.
#
# Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have
# been merged.
#
# The input list is not necessarily ordered in any way.
#
# For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].


def merge_intervals(intervals: list) -> list:
    if not intervals:
        return []
    if len(intervals) == 1:
        return intervals

    sorted_ints = sorted(intervals)
    start = None
    end = None
    res = []
    for i in range(len(sorted_ints) - 1):  # i: range(1)
        cur = sorted_ints[i]
        nxt = sorted_ints[i + 1]
        if not start:
            start = cur[0]
            end = cur[1]

        if end > nxt[0]:
            end = max(end, nxt[1])
        else:
            res.append((start, end))
            start = None
            end = None
        if i == len(sorted_ints) - 2:
            if not start:
                res.append(nxt)
            else:
                res.append((start, end))

    return res


assert merge_intervals([]) == []
assert merge_intervals([(1, 3)]) == [(1, 3)]
assert merge_intervals([(1, 3), (2, 4)]) == [(1, 4)]
assert merge_intervals([(1, 3), (4, 8), (6, 7)]) == [(1, 3), (4, 8)]
assert merge_intervals([(1, 3), (5, 8), (4, 10), (20, 25)]) == [(1, 3), (4, 10), (20, 25)]
