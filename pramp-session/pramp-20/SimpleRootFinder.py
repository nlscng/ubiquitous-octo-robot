# In this question we’ll implement a function root that calculates the n’th root of a number. The function takes a
# nonnegative number x and a positive integer n, and returns the positive n’th root of x within an error of 0.001 (
# i.e. suppose the real root is y, then the error is: |y-root(x,n)| and must satisfy |y-root(x,n)| < 0.001).
#
# Don’t be intimidated by the question. While there are many algorithms to calculate roots that require prior
# knowledge in numerical analysis (some of them are mentioned here), there is also an elementary method which doesn’t
# require more than guessing-and-checking. Try to think more in terms of the latter.
#
# Make sure your algorithm is efficient, and analyze its time and space complexities.
#
# Examples:
#
# input:  x = 7, n = 3
# output: 1.913
#
# input:  x = 9, n = 2
# output: 3

TOLERANCE = 0.01

def power(base, power):
    res = 1
    while power > 0:
        res *= base
        power -= 1

    return res


def is_valid(x, test):
    return x - TOLERANCE <= test < x + TOLERANCE


def root(x, n):
    lower, upper = 1, x  # optimize?

    # binary search
    mid = float(upper + lower) / 2  # 3
    out = power(mid, n)
    while lower < upper:
        if is_valid(x, out):
            return mid
        if out > x:
            upper = mid
        else:
            lower = mid

        mid = float(upper + lower) / 2
        out = power(mid, n)

    return None


assert is_valid(2, root(4, 2))
assert is_valid(3, root(27, 3))
assert is_valid(2, root(16, 4))
assert is_valid(1.732, root(3, 2))
assert is_valid(2.154, root(10, 3))
assert is_valid(5.429, root(160, 3))
