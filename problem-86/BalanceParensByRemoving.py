# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed to make
# the string valid (i.e. each open parenthesis is eventually closed).
#
# For example, given the string "()())()", you should return 1. Given the string ")(", you should return 2,
# since we must remove all of them.

'''
)()

unb = 0
op = 1

'''

def remove_to_balance(s: str) -> int:
    if not s:
        return 0

    if len(s) == 1:
        return 1

    unb = 0
    open_paren = 0
    for i in s:
        if i == '(':
            open_paren += 1
        elif open_paren > 0:
            open_paren -= 1
        else:
            unb += 1

    return unb + open_paren


assert remove_to_balance("") == 0
assert remove_to_balance('(') == 1
assert remove_to_balance(')') == 1
assert remove_to_balance('()') == 0
assert remove_to_balance(')(') == 2
assert remove_to_balance('()())()') == 1
