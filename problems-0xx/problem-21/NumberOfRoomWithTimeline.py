# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Snapchat.
#
# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum
# number of rooms required.
#
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

def minimum_rooms(liz: []):
    """
    Given a list of tuples that indicate start time and end time, return the minimum number for rooms for the schedule
    :param liz:
    :return: int
    """

    def find_max(liz: list):
        cur_max = 0
        for i in range(len(liz)):
            a, b = liz[i]
            cur_max = max(cur_max, a, b)

        return cur_max

    schedule = [0] * find_max(liz)

    for i in range(len(liz)):
        (start, end) = liz[i]
        schedule[start:end + 1] = [x + 1 for x in schedule[start:end + 1]]

    return max(schedule)


assert minimum_rooms([(30, 75), (0, 50), (60, 150)]) == 2
