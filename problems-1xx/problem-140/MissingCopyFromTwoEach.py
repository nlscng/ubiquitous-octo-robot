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

# GG: this turns out to be another XOR problem. I think the space complexity of O(1) is a clue.
# SEE: https://medium.com/@gurupad93/two-numbers-that-appear-once-b89e92a9334b

