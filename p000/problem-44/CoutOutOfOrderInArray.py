# This problem was asked by Google.
#
# We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i]
# and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.
#
# Given an array, count the number of inversions it has. Do this faster than O(N^2) time.
#
# You may assume each element in the array is distinct.
#
# For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1),
# and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.


def merge(a_tup: tuple, b_tup: tuple):
    # REF: https://github.com/vineetjohn/daily-coding-problem/blob/master/solutions/problem_044.py
    memo = []
    a, a_count = a_tup
    b, b_count = b_tup
    ood_count = a_count + b_count  # out of order counter so far from two sub list
    walker_a, walker_b, end_a, end_b = 0, 0, len(a), len(b)
    while walker_a < end_a and walker_b < end_b:
        if a[walker_a] <= b[walker_b]:
            memo.append(a[walker_a])
            walker_a += 1
        else:
            memo.append(b[walker_b])
            ood_count += end_a - walker_a  # wow, such gocha, this is not simply plus one
            walker_b += 1
    while walker_a < end_a:
        memo.append(a[walker_a])
        walker_a += 1
    while walker_b < end_b:
        memo.append(b[walker_b])
        walker_b += 1
    return memo, ood_count


def mergesort(arr: list):
    if not isinstance(arr, list):
        raise Exception('Expected a list, got {} instead.'.format(type(arr)))
    if len(arr) <= 1:
        return arr, 0

    m = len(arr) // 2
    res, ood_count = merge(mergesort(arr[:m]), mergesort(arr[m:]))
    return res, ood_count


assert mergesort([])[0] == []
assert mergesort([3])[0] == [3]
assert mergesort([1, 1])[0] == [1, 1], "actual: {}".format(mergesort([1, 1]))
assert mergesort([1, 2])[0] == [1, 2]
assert mergesort([2, 1])[0] == [1, 2]
assert mergesort([3, 2, 1])[0] == [1, 2, 3]
assert mergesort([2, 1, 3])[0] == [1, 2, 3]
assert mergesort([3, 4, 1, 2])[0] == [1, 2, 3, 4]
assert mergesort([4, 3, 2, 1])[0] == [1, 2, 3, 4]


def count_out_of_order(arr: list):
    # the ideas is, to figure out how many "out of order" there are, we have to compare them, and since
    # we have to compare them, we could just note all the comparing that needs to be done during sorting that
    # is "out of order".
    # and there are many sorting that's better than O(n^2)
    _, counter = mergesort(arr)
    return counter


assert count_out_of_order([]) == 0
assert count_out_of_order([1]) == 0
assert count_out_of_order([1, 2]) == 0
assert count_out_of_order([2, 4, 1, 3, 5]) == 3
assert count_out_of_order([5, 4, 3, 2, 1]) == 10
assert count_out_of_order([2, 6, 1, 3, 7]) == 3
