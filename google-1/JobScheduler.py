"""
Given a job start time, its duration, and an existing schedule, determine if this job can be successfully scheduled.

[[3, 12], [20, 44], [60, 87]]

start time: x
dur: 6
dur: 8
dur: 20


modified binary search,
"""


# GG: this is a modified binary search, an excellent mind twister on something that's so simple and familiar. One of
#  the key thing to realize is, when modifying binary search, I should be actively searching for the valid target,
#  instead of the negative of invalid target.


def fits(outer: [], target: []) -> bool:
    # inclusive test on both boundaries
    return outer[0] <= target[0] <= outer[1] and outer[0] <= target[1] <= outer[1]


def schedule_job_with_start(start: int, dur: int, lis: list) -> bool:
    assert dur > 0 and lis
    end = start + dur - 1
    if end < lis[0][0]:
        return True
    elif start > lis[-1][1]:
        return True

    l, r = 0, len(lis) - 1
    m = (l + r) // 2

    while l <= r:
        # m, the mid point for normal binary search, here its pointed to the left occupied time slot
        if fits([lis[m][1] + 1, lis[m + 1][0] - 1], [start, end]):
            return True
        # if fits(lis[m], [start, end]) or fits(lis[m + 1], [start, end]):
        if start <= lis[m][1] <= end or start <= lis[m][1] <= end:
            return False

        if lis[m + 1][1] < start:
            l = m + 1
            m = (l + r) // 2
        else:
            r = m - 1
            m = (l + r) // 2
    return False


s = [[3, 12], [20, 44], [60, 87]]
assert schedule_job_with_start(0, 2, s)
assert schedule_job_with_start(0, 3, s)
assert schedule_job_with_start(88, 8, s)

assert schedule_job_with_start(13, 2, s)
assert schedule_job_with_start(13, 7, s)
assert schedule_job_with_start(59, 1, s)

assert not schedule_job_with_start(2, 5, s)
assert not schedule_job_with_start(44, 2, s)
assert not schedule_job_with_start(10, 30, s)
assert not schedule_job_with_start(87, 1, s)
