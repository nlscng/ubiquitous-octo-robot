# This problem was asked by Yelp.
#
# Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the
# number could represent. You can assume each valid number in the mapping is a single digit.
#
# For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should return [“ad”, “ae”, “af”, “bd”, “be”,
# “bf”, “cd”, “ce”, “cf"].

'''
2: a b c
3: d e f
'23'




'''


def combo(bank: {}, digit_str: str) -> list:
    # GG: a little mind twisting if you get stuck on the variable number of for loops needed
    if not bank or not digit_str:
        return []

    if len(digit_str) == 1:
        return bank[digit_str[0]]

    my_letters = bank[digit_str[0]]
    rest = combo(bank, digit_str[1:])
    res = []
    for one_letter in my_letters:
        for one_combo in rest:
            res.append(one_letter + one_combo)

    return res


test_bank = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f']
}

assert combo({}, '2') == []
assert combo(test_bank, '') == []
assert combo(test_bank, '2') == ['a', 'b', 'c']
assert combo(test_bank, '23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']


