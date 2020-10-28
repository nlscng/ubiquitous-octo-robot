# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or
# less. You must break it up so that words don't break across lines. Each line has to have the maximum possible
# amount of words. If there's no way to break the text up, then return null.
#
# You can assume that there are no spaces at the ends of the string and that there is exactly one space between each
# word.
#
# For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return: ["the
# quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.


def break_line(src: str, k: int) -> list:
    if not str:
        return None

    tokens = src.split()
    res = []
    cur_line = ''

    for one_token in tokens:
        if len(one_token) >= k:
            return None
        elif len(cur_line) == 0:
            cur_line += one_token
        elif len(cur_line) + len(one_token) + 1 <= k:
            cur_line += ' '
            cur_line += one_token
        else:
            res.append(cur_line)
            cur_line = one_token

    if len(cur_line) > 0:
        res.append(cur_line)

    return res


assert break_line('one', 5) == ['one']
assert break_line('the quick brown fox jumps over the lazy dog', 10) == \
       ["the quick", "brown fox", "jumps over", "the lazy", "dog"]
