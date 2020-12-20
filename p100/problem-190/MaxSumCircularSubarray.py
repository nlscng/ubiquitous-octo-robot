# Given a circular array, compute its maximum subarray sum in O(n) time. A subarray can be empty, and in this case
# the sum is 0.
#
# For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4, and 8 where the 8 is obtained from
# wrapping around.
#
# Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.

"""
At first the circular part confused me a little, but I think can be reduced to two identical, normal array concated
to each other, and do a regular two pointers for max sum subarray. And that's O(n)

8, -1, 3, 4, 8, -1, 3, 4
                         s
                           f

cur 7
max 15

"""

from typing import List


def max_sum_circular_subarray(lis: List[int]) -> int:
    assert lis

    # test for edge case where there are no negatives in the list, if so, just return the whole sum
    if all([x >= 0 for x in lis]):
        return sum(lis)

    n = len(lis)
    slow, fast = 0, 0
    cur_sum, max_sum = 0, 0

    my_lis = lis + lis
    assert len(my_lis) == 2 * n

    while slow < 2 * n:
        # scan ahead and gobble up all the non-negatives
        while fast < 2 * n and my_lis[fast] >= 0:
            cur_sum += my_lis[fast]
            max_sum = max(max_sum, cur_sum)
            fast += 1

        # at this point, fast is at a negative, or is out of bound
        slow = fast
        # scan ahead for next positive numbers and restart the process
        fast += 1
        while fast < 2 * n and my_lis[fast] < 0:
            fast += 1
        cur_sum = 0

    return max_sum


assert max_sum_circular_subarray([8, -1, 3, 4]) == 15
assert max_sum_circular_subarray([-4, 5, 1, 0]) == 6
assert max_sum_circular_subarray([3, 2, 1]) == 6
