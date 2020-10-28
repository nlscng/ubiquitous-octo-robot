# Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50 (but
# also not 0-100 or 100-0). You do not know the bias of the coin.

import random as rand

sample_size = 100000
bias_head_prob = 0.6
bias_exp_value = 2 * bias_head_prob - 1
tolerance = 0.05  ## 10%


def toss_biased():
    return 1 if rand.random() < bias_head_prob else -1


def avg(array: list):
    return sum(array) / len(array)


# print("biased average: {0}".format(sum([toss_biased() for i in range(sample_size)]) / sample_size))
biased_avg = avg([toss_biased() for i in range(sample_size)])
print("biased coin toss {} times, avg {}".format(sample_size, biased_avg))
assert (1 - tolerance) * bias_exp_value < biased_avg < (1 + tolerance) * bias_exp_value


def fair_toss():
    # text book version, the correct version
    coin_1, coin_2 = 1, 1
    while coin_1 == coin_2:
        coin_1 = toss_biased()
        coin_2 = toss_biased()

    return coin_1


fair_avg = avg([fair_toss() for i in range(sample_size)])
print("simulated fair coin toss {} times, avg {}".format(sample_size, fair_avg))
assert -tolerance < fair_avg < tolerance


def wonky_toss():
    maybe = rand.choice([1, -1])
    return maybe * toss_biased()

wonky_avg = avg([wonky_toss() for i in range(sample_size)])
print("wonky, half the time take the value, half the time flipping toss avg {}".format(wonky_avg))
assert -tolerance < fair_avg < tolerance