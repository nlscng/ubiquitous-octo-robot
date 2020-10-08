# You are given n numbers as well as n probabilities that sum up to 1. Write a function to generate one of the
# numbers with its corresponding probability.
#
# For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2], your function should return 1
# 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.
#
# You can generate random numbers between 0 and 1 uniformly.

"""
This seems relative straightforward. I can generate a random value between [0, 1), then compare it to the given numbers
"""
import random
from collections import defaultdict

random.seed(42)


def random_with_distribution(lis: list, probs: list) -> float:
    assert lis and probs and len(lis) == len(probs)

    r = random.random()

    idx = 0
    distribution_sum = 0
    while idx < len(lis):
        distribution_sum += probs[idx]
        if r < distribution_sum:
            return lis[idx]
        idx += 1
    return lis[-1]


random_values = [1, 2, 3, 4]
random_distri = [0.1, 0.5, 0.2, 0.2]
num_runs = 10000
count = defaultdict(int)
for _ in range(num_runs):
    x = random_with_distribution(random_values, random_distri)
    count[x] += 1

print("distributions: {}".format(random_distri))
print("result: {}".format([count[x] / num_runs for x in random_values]))
print(count)