# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Two Sigma.
#
# Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, implement a
# function rand5() that returns an integer from 1 to 5 (inclusive).

import random


def rand7() -> int:
    return random.randint(1, 7)

def sim_rand5() -> int:
    memo = [[1,2,3,4,5,1,2],
            [3,4,5,1,2,3,4],
            [5,1,2,3,4,5,1],
            [2,3,4,5,1,2,3],
            [4,5,1,2,3,4,5],
            [1,2,3,4,5,1,2],
            [3,4,5,0,0,0,0]]
    res = memo[rand7() -1][rand7() -1]
    while res == 0:
        res = memo[rand7() - 1][rand7() - 1]
    return res


test_out = [sim_rand5() for _ in range(1000)]
test_avg = sum(test_out) / 1000
assert 2.9 <= test_avg <= 3.1, 'Actual: {}'.format(test_avg)
