# This problem was asked by Google.
#
# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
#
# Hint: The basic equation of a circle is x2 + y2 = r2.

##Google

import random as rand
from math import pi


def find_pi():
    x = rand.random()
    y = rand.random()
    return x ** 2 + y ** 2 < 1


def monte_carlo_find_pi(times: int):
    sims = [find_pi() for i in range(times)]
    return sum(sims) / len(sims) * 4


num_sims = 1000000
print("monte carlo finding pi: {}".format(monte_carlo_find_pi(num_sims)))
assert 0.95 * pi < monte_carlo_find_pi(num_sims) < 1.05 * pi
