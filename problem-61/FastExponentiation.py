# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns
# x^y.
#
# Do this faster than the naive method of repeated multiplication.
#
# For example, pow(2, 10) should return 1024.

import time

def fast_exp(n: int, p: int) -> int:
    memo = {0: 1, 1: n}
    if p < 2:
        return memo[p]

    def fill_memo():
        i = 1
        while i < p:
            j = i + i
            memo[j] = memo[i] * memo[i]
            i = j

    def max_usable_power(r: int, ks: list) -> int:
        for idx in range(len(ks)):
            if ks[idx] > r:
                return ks[idx - 1]
            if ks[idx] == r:
                return ks[idx]
        raise Exception('Failed to find max usable power in memo')

    fill_memo()
    keys = sorted(list(memo.keys()))
    remainder = p
    res = 1
    while remainder > 0:
        next_power = max_usable_power(remainder, keys)
        res *= memo[next_power]
        remainder -= next_power

    return res


def brute_force_power(n: int, p: int) -> int:
    res = 1
    while p > 0:
        res *= n
        p -= 1
    return res


assert fast_exp(2, 1) == 2
assert fast_exp(2, 0) == 1
assert fast_exp(2, 2) == 4
assert brute_force_power(2, 2) == 4


BASE = 13
POWER = 10000

f_start = time.time()
assert fast_exp(BASE, POWER) == pow(BASE, POWER)
f_end = time.time()
f_dur = f_end - f_start

b_start = time.time()
assert brute_force_power(BASE, POWER) == pow(BASE, POWER)
b_end = time.time()
b_dur = b_end - b_start

assert b_dur > f_dur
