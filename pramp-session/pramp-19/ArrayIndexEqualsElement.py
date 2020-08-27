# Given a sorted array arr of distinct integers, write a function indexEqualsValueSearch that returns the lowest index i for which arr[i] == i. Return -1 if there is no such index. Analyze the time and space complexities of your solution and explain its correctness.
#
# Examples:
#
# input: arr = [-8,0,2,5]
# output: 2 # since arr[2] == 2
#
# input: arr = [-1,0,3,6]
# output: -1 # since no index in arr satisfies arr[i] == i.


def index_equals_value_search(arr):
    # safety check

    # corner case base case
    if not arr:
        return -1

    if len(arr) == 1:
        return 0 if arr[0] == 0 else -1

    # we have arr len > 1
    left = 0
    right = len(arr)  # exclusive # 1

    cur_match = 9999999
    # iter
    while left <= right:
        mid = (left + right) // 2  # 0
        if mid == arr[mid]:
            if mid < cur_match:
                cur_match = mid
            # move right ptr
            right = mid - 1
        elif arr[mid] > mid:
            right = mid - 1
        else:
            left = mid + 1
    return -1 if cur_match == 9999999 else cur_match


assert index_equals_value_search([0]) == 0
assert index_equals_value_search([0, 3]) == 0
assert index_equals_value_search([-8, 0, 1, 3, 5]) == 3
assert index_equals_value_search([-5, 0, 2, 3, 10, 29]) == 2
assert index_equals_value_search([-5, 0, 3, 4, 10, 18, 27]) == -1
assert index_equals_value_search([-6, -5, -4, -1, 1, 3, 5, 7]) == 7
