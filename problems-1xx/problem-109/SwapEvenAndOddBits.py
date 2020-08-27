# This problem was asked by Cisco.
#
# Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and 2nd bit should be swapped, the 3rd and 4th
# bit should be swapped, and so on.
#
# For example, 10101010 should be 01010101. 11100010 should be 11010001.
#
# Bonus: Can you do this in one line?


'''
1010 1010 -> 0101 0101
128  + 32  +8 + 2 -> 64 + 16 + 4 + 1

170 -> 85

naive approach is to iterate and swap every two bits, this is linear, which isn't too bad, but better solution
uses bit mask to do all in constant time


'''

# GG: it's rare to work on bit manipulation, remember masking is usually one option

def swap_bits(b):
    even = b & 0b10101010
    odds = b & 0b01010101
    even_shifted = even >> 1
    odds_shifted = odds << 1
    return even_shifted | odds_shifted


assert swap_bits(170) == 85
