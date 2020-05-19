# Given two sorted arrays arr1 and arr2 of passport numbers, implement a function findDuplicates that returns an
# array of all passport numbers that are both in arr1 and arr2. Note that the output array should be sorted in an
# ascending order.
#
# Let N and M be the lengths of arr1 and arr2, respectively. Solve for two cases and analyze the time & space
# complexities of your solutions: M ≈ N - the array lengths are approximately the same M ≫ N - arr2 is much bigger
# than arr1.

def find_duplicates(arr1, arr2):
    # this is O(n + m) in time and O(1) in space
    n = len(arr1)
    m = len(arr2)
    walker_1, walker_2 = 0, 0
    res = []

    while walker_1 < n and walker_2 < m:
        if arr1[walker_1] == arr2[walker_2]:
            res.append(arr1[walker_1])
            walker_1 += 1
            walker_2 += 1
        elif arr1[walker_1] < arr2[walker_2]:
            walker_1 += 1
        else:
            walker_2 += 1

    return res


assert find_duplicates([], []) == []
assert find_duplicates([1], [1]) == [1]
assert find_duplicates([1, 2, 3, 5, 6, 7], [3, 6, 7, 8, 20]) == [3, 6, 7]


def binary_search(k: int, arr: list):
    if not arr:
        return False
    elif k == arr[0]:
        return True
    else:
        mid = len(arr) // 2
        if k == arr[mid]:
            return True
        elif k > arr[mid]:
            return binary_search(k, arr[mid+1:])
        else:
            return binary_search(k, arr[:mid])


assert binary_search(5, [5])
assert not binary_search(1, [])
assert binary_search(5, [1, 2, 5, 6, 8, 9])


def find_duplicate_one_huge_list(arr1, arr2):
    # assume arr2 is very very very large
    # then we use binary search to break down m into log m
    n = len(arr1)
    m = len(arr2)

    res = []
    for one_ele in arr1:
        if binary_search(one_ele, arr2):
            res.append(one_ele)

    return res


assert find_duplicate_one_huge_list([], []) == []
assert find_duplicate_one_huge_list([1], [1]) == [1]
assert find_duplicate_one_huge_list([1, 2, 3, 5, 6, 7], [3, 6, 7, 8, 20]) == [3, 6, 7]
