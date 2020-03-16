# This problem was asked by Facebook.
#
# Given a stream of elements too large to store in memory, pick a random element from the stream with uniform
# probability.

import random as rand


def reservoir_sample(stream: list, k: int):
    found = [None] * k
    for i in range(len(stream)):
        idx = rand.randrange(i)
        if idx < k:
            found[idx] = stream[i]

    return found
