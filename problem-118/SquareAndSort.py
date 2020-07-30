# This problem was asked by Google.
#
# Given a sorted list of integers, square the elements and give the output in sorted order.
#
# For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].


"""
Interesting problem.

-9, -2, 0, 2, 3
        l
        r
0, 4, 4, 9, 81

81 , 9, 4, 4

Since the given list is sorted, I think I can use two pointers walking toward the middle to do this in one scan


"""


# GG: this is relative simple, maybe a 1st round interview question

def square_and_sort(arr: list) -> list:
    if not arr:
        return []
    if len(arr) == 1:
        return [arr[0] ** 2]

    n = len(arr)
    l_walker, r_walker = 0, n - 1  # both walkers are inclusive
    res = []

    while l_walker <= r_walker:
        l_val = abs(arr[l_walker])
        r_val = abs(arr[r_walker])
        if l_val > r_val:
            res.append(l_val ** 2)
            l_walker += 1
        else:
            res.append(r_val ** 2)
            r_walker -= 1

    res.reverse()
    return res


assert square_and_sort([9]) == [81]
assert square_and_sort([2, 3]) == [4, 9]
assert square_and_sort([-3, 1]) == [1, 9]
assert square_and_sort([-9, -2, 0, 2, 3]) == [0, 4, 4, 9, 81]
