# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs
# come first, the Gs come second, and the Bs come last. You can only swap elements of the array.
#
# Do this in linear time and in-place.
#
# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B',
# 'B'].

##GOOGLE
##TBC

def sort_rgb(liz: list):
    if not isinstance(liz, list):
        raise Exception('Expected an list or array, got {} instead.'.format(type(liz)))
    if not liz:
        return []
    if any([x != 'R' and x != 'G' and x != 'B' for x in liz]):
        raise Exception('Expected members to be strictly "R", "G", or "B", but found others.')

    toll = {'R': liz.count('R'), 'G': liz.count('G'), 'B': liz.count('B')}

    for i in range(len(liz)):
        if i < toll['R']:
            liz[i] = 'R'
        elif i < toll['R'] + toll['G']:
            liz[i] = 'G'
        else:
            liz[i] = 'B'

    return liz


assert sort_rgb([]) == []
assert sort_rgb(['R', 'G', 'B']) == ['R', 'G', 'B']
assert sort_rgb(['G', 'B', 'R', 'R', 'B', 'R', 'G']) == ['R', 'R', 'R', 'G', 'G', 'B', 'B']
