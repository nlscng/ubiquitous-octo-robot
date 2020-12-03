# This problem was asked by Amazon.
#
# Given n numbers, find the greatest common denominator between them.
#
# For example, given the numbers [42, 56, 14], return 14.
from typing import List


def find_gcd(nums: List[int]) -> int:
    assert nums
    stop = min(nums)

    gcd = 1
    walker = 2
    while walker <= stop:
        remainders = [x % walker for x in nums]
        if sum(remainders) == 0:
            nums = [x / walker for x in nums]
            gcd *= walker
            stop /= walker
            walker -= 1
        walker += 1
    return gcd


assert find_gcd([42, 56, 14]) == 14
assert find_gcd([8, 64, 32]) == 8
assert find_gcd([93, 73, 89]) == 1