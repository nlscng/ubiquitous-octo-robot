# This problem was asked by Amazon.
#
# Implement a bit array.
#
# A bit array is a space efficient array that holds a value of 1 or 0 at each index.
#
# init(size): initialize the array with size
# set(i, val): updates index at i with val where val is either 1 or 0.
# get(i): gets the value at index i.

"""
This feels like a good bit manipulation practice. Firs thing I can think of is, say we 4 byte per int, then that's 32
bits I can store. So saving one bit to index i is equivalent of updating that single bit in a corresponding bit to 1

"""