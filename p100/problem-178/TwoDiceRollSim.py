# This problem was asked by Two Sigma.
#
# Alice wants to join her school's Probability Student Club. Membership dues are computed via one of two simple
# probabilistic games.
#
# The first game: roll a die repeatedly. Stop rolling once you get a five followed by a six. Your number of rolls is
# the amount you pay, in dollars.
#
# The second game: same, except that the stopping condition is a five followed by a five.
#
# Which of the two games should Alice elect to play? Does it even matter? Write a program to simulate the two games
# and calculate their expected value.

"""
This conceptually should be the same.
"""

import random as rand

rand.seed(42)


def num_dice_roll(a: int, b: int) -> int:
    assert 1 <= a <= 6 and 1 <= b <= 6
    num_roll = 0
    while rand.randint(1, 6) != a:
        num_roll += 1
    while rand.randint(1, 6) != b:
        num_roll += 1
    return num_roll


def sim_n_runs(n: int, a: int, b: int) -> float:
    assert n
    assert 1 <= a <= 6 and 1 <= b <= 6
    rolls = []
    for _ in range(n):
        rolls.append(num_dice_roll(a, b))
    return sum(rolls) / n


print('running 1k times')
print(sim_n_runs(1000, 5, 6))
print(sim_n_runs(1000, 5, 5))

print('running 10k times')
print(sim_n_runs(10000, 5, 6))
print(sim_n_runs(10000, 5, 5))
