# Given a list, sort it using this method: reverse(lst, i, j), which reverses lst from i to j.

"""
Not sure where to start...

Brute force would be like this. Consider an already sorted list, then a new element at index j (just outside the already
sorted list) should be sorted right after the i-th index, then we need to rev list[i .. j-1], then rev [i .. j]
This is most likely not very efficient. But that's code this up anyway.

The naive version is O(n^2) in time

"""


# GG: apparently this is also called pancake sort, like you want to sort a vertically stacked pancakes

# LOST

def rev(lst: list, i: int, j: int) -> list:
    # given a list, reverse from index i to j, j inclusive
    assert lst and 0 <= i <= j < len(lst)
    head = lst[:i]
    body = lst[i:j + 1]
    tail = lst[j + 1:]
    return head + body[::-1] + tail


assert rev([1, 2, 3, 4], 0, 3) == [4, 3, 2, 1]
assert rev([1, 2, 3, 4], 1, 2) == [1, 3, 2, 4]


def is_sorted(lst: list) -> bool:
    assert lst
    if len(lst) == 1:
        return True

    for idx in range(1, len(lst)):
        if lst[idx] < lst[idx - 1]:
            return False
    return True


assert is_sorted([1])
assert is_sorted([1, 2])
assert is_sorted([1, 1])
assert not is_sorted([2, 1])


def find_index(lst: list, k: int) -> int:
    # Given a list and an element k that should go into this list, find the index which k should be insert into
    assert lst
    for idx in range(len(lst)):
        if lst[idx] > k:
            return idx
    return len(lst)


assert find_index([1], 2) == 1
assert find_index([1], 0) == 0
assert find_index([1, 3], 2) == 1
assert find_index([1, 2], 2) == 2


def sort_by_rev_naive(lst: list) -> list:
    assert lst
    n = len(lst)

    if n == 1:
        return lst

    for idx in range(1, n):
        if not is_sorted(lst[:idx + 1]):
            k = lst[idx]
            k_target_idx = find_index(lst, k)
            lst = rev(lst, k_target_idx, idx - 1)
            lst = rev(lst, k_target_idx, idx)

    return lst


assert sort_by_rev_naive([1]) == [1]
assert sort_by_rev_naive([1, 2]) == [1, 2]
assert sort_by_rev_naive([1, 2, 3]) == [1, 2, 3]
assert sort_by_rev_naive([2, 1]) == [1, 2]
assert sort_by_rev_naive([3, 2, 1]) == [1, 2, 3]
assert sort_by_rev_naive([3, 2, 4, 1]) == [1, 2, 3, 4]
