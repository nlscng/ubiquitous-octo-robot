# This problem was asked by Google.
#
# You are given a starting state start, a list of transition probabilities for a Markov chain, and a number of steps num_steps. Run the Markov chain starting from start for num_steps and compute the number of times we visited each state.
#
# For example, given the starting state a, number of steps 5000, and the following transition probabilities:
#
# [
#   ('a', 'a', 0.9),
#   ('a', 'b', 0.075),
#   ('a', 'c', 0.025),
#   ('b', 'a', 0.15),
#   ('b', 'b', 0.8),
#   ('b', 'c', 0.05),
#   ('c', 'a', 0.25),
#   ('c', 'b', 0.25),
#   ('c', 'c', 0.5)
# ]
# One instance of running this Markov chain might produce { 'a': 3012, 'b': 1656, 'c': 332 }.

# GG: this is a stationary markov chain distribution problem, GT lectures covered the basis for it.

# GG: good question to review

import pandas as pd


def to_adj_list(matrix: list, keys: list) -> list:
    assert matrix
    n = len(keys)
    key_idx = {k: i for i, k in enumerate(keys)}
    res = [[0 for _ in range(n)] for _ in range(n)]
    for one_entry in matrix:
        src, snk, prob = one_entry
        src_idx = key_idx[src]
        snk_idx = key_idx[snk]
        res[src_idx][snk_idx] = prob
    return res


m1 = [
    ('a', 'a', 0.9),
    ('a', 'b', 0.075),
    ('a', 'c', 0.025),
    ('b', 'a', 0.15),
    ('b', 'b', 0.8),
    ('b', 'c', 0.05),
    ('c', 'a', 0.25),
    ('c', 'b', 0.25),
    ('c', 'c', 0.5)
]
print(to_adj_list(m1, ['a', 'b', 'c']))


def markov_chain_n_step(matrix: list, n: int) -> list:
    assert matrix and n and isinstance(matrix[0], tuple)
    keys = sorted(set([k for k, _, _ in matrix]))
    adj_list = to_adj_list(matrix, keys)

    df = pd.DataFrame(adj_list)
    res = df
    for _ in range(n):
        res = res @ df

    print('res ' + str(res))

    return (res.iloc[0, :] * n).tolist()


print(markov_chain_n_step(m1, 5000))
