# This problem was asked by Amazon.
#
# Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated
# successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as
# "4A3B2C1D2A".
#
# Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists
# solely of alphabetic characters. You can assume the string to be decoded is valid.

'''
aaabbcda
s
   *

a
s
 f

count =

'''

def run_length(in_str: str) -> str:
    if not in_str:
        return ''
    res = ''
    slow, fast, s_len = 0, 0, len(in_str)

    while slow < s_len:
        while fast < s_len and in_str[slow] == in_str[fast]:
            fast += 1
        count = fast - slow
        res += str(count) + in_str[slow]
        slow += 1

    return res


assert run_length('') == ''
assert run_length('a') == '1a'
assert run_length('aa') == '2a'
assert run_length('abc') == '1a1b1c'
assert run_length('aaaabbbccdaa') == '4a3b2c1d2a'

