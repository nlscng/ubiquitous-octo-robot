# This problem was asked by Amazon.
#
# You are given a list of data entries that represent entries and exits of groups of people into a building. An entry
# looks like this:
#
# {"timestamp": 1526579928, count: 3, "type": "enter"}
#
# This means 3 people entered the building. An exit looks like this:
#
# {"timestamp": 1526580382, count: 2, "type": "exit"}
#
# This means that 2 people exited the building. timestamp is in Unix time.
#
# Find the busiest period in the building, that is, the time with the most people in the building. Return it as a
# pair of (start, end) timestamps. You can assume the building always starts off and ends up empty, i.e. with 0
# people inside.

"""
First glance, this feels like a time series problem where I am to find the biggest diff between two time slots.
Take the follow seq of numbers, positive for entering, negative for exiting:

5, 3, -4, 2, -6

5, -4, 3, 2, -6

Second glance, and a little googling, I've decided the term 'busiest period' needs a lot more clarification. Another point that needs clarifying, is if the events comes in sorted, I think it might make sense to assume it's sorted

"""

import sys
from collections import defaultdict


def busiest_time(events: list) -> list:
    assert events

    ts_enter = defaultdict(int)
    ts_exit = defaultdict(int)
    for e in events:
        ts, num, type = e['ts'], e['count'], e['type']
        if type == 'enter':
            ts_enter[ts] = num
        else:
            ts_exit[ts] = num

    cur_count = 0
    max_count = -sys.maxsize
    start_t, end_t = 0, None
    for e in events:
        t = e['ts']
        if t in ts_enter:
            cur_count += ts_enter[t]
        elif t in ts_exit:
            cur_count -= ts_exit[t]

        if t in ts_enter or t in ts_exit:
            if cur_count > max_count:
                start_t = t
                end_t = None
                max_count = cur_count
            elif cur_count < max_count and end_t is None:
                end_t = t

    return [start_t, end_t]


schedule_1 = [{'ts': 32, 'count': 5, 'type': 'enter'},
              {'ts': 48, 'count': 2, 'type': 'exit'},
              {'ts': 49, 'count': 3, 'type': 'enter'},
              {'ts': 57, 'count': 5, 'type': 'enter'},
              {'ts': 70, 'count': 11, 'type': 'exit'}]
assert busiest_time(schedule_1) == [57, 70]

schedule_2 = [{'ts': 32, 'count': 10, 'type': 'enter'},
              {'ts': 48, 'count': 2, 'type': 'exit'},
              {'ts': 49, 'count': 1, 'type': 'enter'},
              {'ts': 57, 'count': 6, 'type': 'exit'},
              {'ts': 70, 'count': 3, 'type': 'exit'}]
assert busiest_time(schedule_2) == [32, 48]
