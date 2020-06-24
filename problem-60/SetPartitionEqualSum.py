# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.
#
# For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into {
# 15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.
#
# Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets that add
# up to the same sum.

'''
1, 1, 2
   l
    r
ls = 1
rs = 2
'''

def partition_sum_equal(nums: list) -> bool:
    # this is O(n log n) because the sort, the two pointers takes O(n) time, and O(1) space
    if not nums or len(nums) == 1:
        return False

    nums_sorted = sorted(nums)
    lptr, rptr = 0, len(nums) - 1
    lsum, rsum = 0, 0

    while lptr <= rptr:
        if lsum <= rsum:
            lsum += nums_sorted[lptr]
            lptr += 1
        else:
            rsum += nums_sorted[rptr]
            rptr -= 1

    return lsum == rsum


assert not partition_sum_equal([])
assert not partition_sum_equal([1])
assert partition_sum_equal([1, 1])
assert partition_sum_equal([1, 2, 1])
assert partition_sum_equal([1, 1, 1, 1])
assert partition_sum_equal([15, 5, 20, 10, 35, 15, 10])
assert not partition_sum_equal([15, 5, 20, 10, 35])
