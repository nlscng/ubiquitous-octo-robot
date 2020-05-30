# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Two Sigma.
#
# Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a
# function rand7() that returns an integer from 1 to 7 (inclusive).
#
import random


def rand_5() -> int:
    return random.randint(1, 5)


def rand_7() -> int:
    lookup = [[1, 2, 3, 4, 5],
              [6, 7, 1, 2, 3],
              [4, 5, 6, 7, 1],
              [2, 3, 4, 5, 6],
              [7, 0, 0, 0, 0]]
    res = 0
    while res == 0:
        res = lookup[rand_5() - 1][rand_5() - 1]

    return res


num_runs = 100000
test_res = [rand_7() for _ in range(num_runs)]
avg = float(sum(test_res)) / num_runs
assert 3.9 < avg < 4.1, 'Actual: {}'.format(avg)
