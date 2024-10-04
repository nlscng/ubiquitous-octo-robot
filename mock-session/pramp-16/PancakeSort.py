# Pancake Sort
# Given an array of integers arr:
#
# Write a function flip(arr, k) that reverses the order of the first k elements in the array arr. Write a function
# pancakeSort(arr) that sorts and returns the input array. You are allowed to use only the function flip you wrote in
# the first step in order to make changes in the array. Example:
#
# input:  arr = [1, 5, 4, 3, 2]
#
# output: [1, 2, 3, 4, 5] # to clarify, this is pancakeSort's output
# Analyze the time and space complexities of your solution.
#
# Note: it’s called pancake sort because it resembles sorting pancakes on a plate with a spatula, where you can only
# use the spatula to flip some of the top pancakes in the plate. To read more about the problem, see the Pancake
# Sorting Wikipedia page.

def flip(array, k) -> list:
    # this k is exclusive, so we flip up to but not include the k-th element
    return array[:k][::-1] + array[k:]


assert flip([1, 2, 3], 3) == [3, 2, 1]
assert flip([1, 2, 3], 2) == [2, 1, 3]
assert flip([1], 1) == [1]


def pancake_sort(arr):
    for idx in range(len(arr)):  # idx 1
        cur_min = min(arr[idx:])  # 1
        min_idx = arr[idx:].index(cur_min)  # 1
        if arr[idx] != cur_min:
            arr = arr[:idx] + flip(arr[idx:], min_idx + 1)
            print("idx : {}, arr: {}".format(idx, arr))
    return arr


# assert pancake_sort([1,2]) == [1,2]
assert pancake_sort([1, 3, 1]) == [1, 1, 3]
assert pancake_sort([3, 1, 2, 4, 6, 5]) == [1, 2, 3, 4, 5, 6]
assert pancake_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert pancake_sort([10, 9, 8, 6, 7, 5, 4, 3, 2, 1, 9, 10, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [
    1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]
