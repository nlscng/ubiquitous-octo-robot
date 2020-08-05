# This problem was asked by Facebook.
#
# Write a function that rotates a list by k elements. For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4,
# 5, 6, 1, 2]. Try solving this without creating a copy of the list. How many swap or move operations do you need?


"""

If creating copies is allowed, I can just create another copy, append the original with, then slice it out with k chars
skipped

Only swapping though, it will have to be a O(n) operation, since every element needs to be looked at at least once.
It is linear but it's is really like (n - k) swap needed


1,2,3,4,5,6
*
3,2,1,4,5,6
  *
3,4,1,2,5,6
    *
3,4,5,2,1,6
      *
3,4,5,6,1,2
"""


def rotate_array(arr: list, k: int) -> []:
    if not arr:
        return []

    while k < 0:
        k += len(arr)
    k = k % len(arr) if k > len(arr) else k
    for i in range(len(arr) - k):
        arr[i], arr[i + k] = arr[i + k], arr[i]

    return arr


assert rotate_array([1, 2, 3, 4, 5, 6], 2) == [3, 4, 5, 6, 1, 2]
assert rotate_array([1, 2, 3, 4, 5, 6], -4) == [3, 4, 5, 6, 1, 2]
