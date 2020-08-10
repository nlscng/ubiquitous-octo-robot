# Given a real number n, find the square root of n. For example, given n = 9, return 3.

"""
This is a classic search problem with a known range, so binary search it is

"""


def in_range(f: float, k: float) -> bool:
    tolerance = 0.001
    return f - tolerance <= k <= f + tolerance


def sqrt(n: float) -> float:
    assert n > 0

    ub = n / 2
    lb = 0

    t = ((ub + lb) / 2) ** 2
    while not in_range(t, n):
        if t < n:
            lb = (ub + lb) / 2
        else:
            ub = (ub + lb) / 2
        t = ((ub + lb) / 2) ** 2

    return (ub + lb) / 2


assert in_range(sqrt(9), 3)
assert in_range(sqrt(25), 5)