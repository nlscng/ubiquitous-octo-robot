# This problem was asked by Apple.
#
# Gray code is a binary code where each successive value differ in only one bit, as well as when wrapping around.
# Gray code is common in hardware so that we don't see temporary spurious values during transitions.
#
# Given a number of bits n, generate a possible gray code for it.
#
# For example, for n = 2, one gray code would be [00, 01, 11, 10].

"""
This is new. Let's try some sample first

if n = 1:
1, 0

if n = 2
00, 01, 11, 10
11, 01, 00, 10

if n = 3:
000, 001, 011, 111, 110, 100

"""