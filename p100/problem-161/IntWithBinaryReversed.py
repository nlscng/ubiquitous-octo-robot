# This problem was asked by Facebook.
#
# Given a 32-bit integer, return the number with its bits reversed.
#
# For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000, return 0000 1111 0000 1111 0000 1111
# 0000 1111.

"""
This should be straighforward, if I know/can find python library built-ins.

So I am changing it to, given an int, return an int that's in binary a mirror image of it.
"""


# GG: interesting exercise. In python, to int -> str, I can do int("0bxxxx", 2) to convert base 2 binary string to
#  int, and to str to bin string, just bin()


def int_of_binary_reversed(k: int) -> int:
    return int('0b' + bin(k)[2:][::-1], 2)


assert int_of_binary_reversed(8) == 1
assert int_of_binary_reversed(11) == 13
