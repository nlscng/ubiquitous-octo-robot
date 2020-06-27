# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# An sorted array of integers was rotated an unknown number of times.
#
# Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't
# exist in the array, return null.
#
# For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).
#
# You can assume all the integers in the array are unique.

'''

left ... mid ... right
      b: > left or < mid => left, else go right
              b: > left and < mid go left, go right


so both scenario relies on the value of left to decide which half to go

'''


def rotated_binary_search(nums: list, k: int) -> int:
    # GG: this is a very interesting binary search exercise
    if not nums:
        return None
    if len(nums) < 2 and nums[0] != k:
        return None

    left = 0
    right = len(nums)

    while left < right:
        mid = (left + right) // 2
        if nums[mid] == k:
            return mid

        if k >= nums[left]:
            right = mid
        else:
            left = mid

    return None


assert rotated_binary_search([], 3) is None
assert rotated_binary_search([1], 3) is None
assert rotated_binary_search([1], 1) == 0
assert rotated_binary_search([1, 3], 3) == 1
assert rotated_binary_search([12, 18, 25, 2, 8, 10], 8) == 4
