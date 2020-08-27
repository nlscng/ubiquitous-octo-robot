# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Microsoft.
#
# Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of
# the list so far on each new element.
#
# Recall that the median of an even-numbered list is the average of the two middle numbers.
#
# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
#
# 2
# 1.5
# 2
# 3.5
# 2
# 2
# 2


def naive_running_med(liz: list):
    if not isinstance(liz, list):
        raise Exception('Expected a list, got {} instead'.format(type(liz)))

    if not liz:
        return 0

    memo = []
    meds = []
    for i in liz:
        memo.append(i)
        memo.sort()
        l = len(memo)
        if l % 2 == 0:
            meds.append((memo[l // 2] + memo[l // 2 - 1]) / 2)
        else:
            meds.append(memo[l // 2])

    return meds


assert naive_running_med([2, 1, 5, 7, 2, 0, 5]) == [2, 1.5, 2, 3.5, 2, 2, 2]
