# Given an array of integers in which two elements appear exactly once and all other elements appear exactly twice,
# find the two elements that appear only once.
#
# For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.
#
# Follow-up: Can you do this in linear time and constant space?

"""
This feels like a kindaichi case file puzzle lol

Normal solution would be to count them with dict, then go through the counts and find ones that has just one copy.
This would cost O(n) in time and O(n) in space

Or use a set, walk through the array, add to set if not seen, remove if it's already in set. This is also O(n) in time
but also O(n) in space

Can I use some type of bit set, which is maybe O(1) in space, to replace the set?
If I do this, I need to find the max and min to know how many byte I need to represent.
Say max is 42, min is greater than 0, then I can use a variable that's at least 42 bit long...
This won't be space efficient ...
But is this really O(1) in space? It feels more like O(log n)
"""


# GG: this turns out to be another XOR problem. I think the space complexity of O(1) is a clue. Probably the best xor
#  problem
# SEE: https://medium.com/@gurupad93/two-numbers-that-appear-once-b89e92a9334b

def uniques_in_dupes(array: list):
    a, b = 0, 0
    xor_all = 0
    for i in array:
        xor_all = xor_all ^ i

    # search for one bit, any bit, that's set to 1, because they can tell the two unique number apart.
    diff_bit_idx = 0
    for i in range(0, 32):
        if xor_all & (1 << i) != 0:  # this is important to use " != 0 ", we are testing for bit wise equality
            diff_bit_idx = i
            break

    # we xor all numbers into two groups, each xor-ing each other in group, again using the fact same number xor-ing
    # themselves will cancel the bits out to zero
    for i in array:
        if i & (1 << diff_bit_idx) == 0:
            a = a ^ i
        else:
            b = b ^ i
    return [a, b]


assert uniques_in_dupes([1, 2, 3, 1]) == [2, 3]
assert uniques_in_dupes([1, 2, 3, 2]) == [1, 3], "Actual: {}".format(uniques_in_dupes([1, 2, 3, 2]))
assert uniques_in_dupes([1, 2, 3, 4, 5, 1, 4, 5]) == [2, 3]
