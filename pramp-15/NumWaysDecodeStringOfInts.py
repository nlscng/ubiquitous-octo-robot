# A letter can be encoded to a number in the following way:
#
# 'A' -> '1', 'B' -> '2', 'C' -> '3', ..., 'Z' -> '26'
# A message is a string of uppercase letters, and it is encoded first using this scheme. For example, 'AZB' -> '1262'
#
# Given a string of digits S from 0-9 representing an encoded message, return the number of ways to decode it.
#
# Examples:
#
# input:  S = '1262'
# output: 3
# explanation: There are 3 messages that encode to '1262': 'AZB', 'ABFB'


def decode_variations(s):
    # this is O(n) in time and O(n) in space
    if not s or len(s) == 1:
        return 1

    memo = [0] * (len(s) + 1) # note the memo table has additional idx of 0 in head
    memo[0] = memo[1] = 1   # there is one way to decode an empty string, and one way to decode single digit string

    for idx in range(1, len(s)):   # idx is index off the string s
        cur_ptr = idx + 1
        pre_ptr = idx   # since our memo[1] is matching the 0th char in string
        snd_pre_ptr = idx - 1 if idx > 0 else None

        if s[idx] == '0':
            if idx > 0 and s[idx - 1] != 2 and s[idx - 1] != 1:
                return 0

        if idx > 0 and 10 <= int(s[idx-1:idx+1]) <= 26:
            if s[idx] == 0: # for the cases of '10' and '20'
                memo[cur_ptr] = memo[pre_ptr]
            else:
                memo[cur_ptr] = memo[pre_ptr] + memo[snd_pre_ptr]
        else:
            memo[cur_ptr] = memo[pre_ptr]

    return memo[-1]


assert decode_variations('1270') == 0

