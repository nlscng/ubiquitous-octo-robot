# This problem was asked by Alibaba.
#
# Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.
#
# A solution will always exist. See Goldbach’s conjecture.
#
# Example:
#
# Input: 4
# Output: 2 + 2 = 4
# If there are more than one solution possible, return the lexicographically smaller solution.
#
# If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then
#
# [a, b] < [c, d]
# If a < c OR a==c AND b < d.
#
#


'''
k = 14
primes = [2, 3, 5, 7, 11]

if I find a list of prime smaller than k, this becomes a subset 2 sum problem, which is linear

'''


# SEE: sieve of Eratosthenes

def find_primes(k: int) -> list:
    # GG: this is somewhat counter-intuitively O(n)
    assert k > 2
    nums = [a for a in range(2, k)]
    is_primes = [True] * (k + 1)  # note the +1 to account for 0 indexed
    is_primes[0] = is_primes[1] = False
    res = []
    for i in range(2, k):
        if is_primes[i]:
            res.append(i)
            mul = i
            while mul <= k:
                is_primes[mul] = False
                mul += i

    return res


assert find_primes(6) == [2, 3, 5]
assert find_primes(14) == [2, 3, 5, 7, 11, 13]


def find_two_prime_sum(k: int) -> tuple:
    assert k > 2 and k % 2 == 0

    primes = find_primes(k)
    remaining = set()
    res = []
    for p in primes:
        if p + p == k:
            res.append((p, p))
        elif p not in remaining:
            remaining.add(k - p)
        else:
            res.append((k - p, p))

    if len(res) > 1:
        res.sort()
    return res[0]


assert find_two_prime_sum(6) == (3, 3)
assert find_two_prime_sum(8) == (3, 5)
assert find_two_prime_sum(14) == (3, 11)
