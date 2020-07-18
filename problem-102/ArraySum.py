# This problem was asked by Lyft.
#
# Given a list of integers and a number K, return which contiguous elements of the list sum to K.
#
# For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.

# GG: need to clarify if this array is sorted, or if the content are all positive. It looks likes both are true here.

'''

if the array are positive and sorted, this is a two pointer/sliding window problem for O(n)
if the array isn't sorted, we might take a hit for O(n log n)

if the array contains negative but is sorted, hmm ...

1,2,3,4,5 -> 9
  l
        r
sum = 10

3, k = 3
l
 r
s = 3

1,2,3,4,5 -> 12
l
          r
s: 15
'''


def array_sum(arr: list, k: int) -> list:
    if not arr or k < 0 or k < min(arr) or min(arr) < 0:
        return []

    l_walker, r_walker, n = 0, 0, len(arr)
    cur_sum = 0
    while (r_walker < n and cur_sum < k) or (l_walker < r_walker and cur_sum > k):  # GG: tricky to get right
        if cur_sum == k:
            return arr[l_walker:r_walker]
        if cur_sum < k:
            cur_sum += arr[r_walker]
            r_walker += 1
        else:
            cur_sum -= arr[l_walker]
            l_walker += 1

    return arr[l_walker:r_walker] if cur_sum == k else []


assert array_sum([], 3) == []
assert array_sum([3, 4, 5], 2) == []
assert array_sum([3], 3) == [3], "Actual: {}".format(array_sum([3], 3))
assert array_sum([1, 2, 3, 4, 5], 9) == [2, 3, 4]
assert array_sum([1, 2, 3, 4, 5], 12) == [3, 4, 5]
