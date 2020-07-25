# This problem was asked by Google.
#
# Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here", return "here world hello"
#
# Follow-up: given a mutable string representation, can you perform this operation in-place?


'''
'hello word here'

'here world hello'

I can reverse the whole thing, letter wise, then scan for words, and reverse those words.
This should be O(n) as I went through the input twice in linear way

'''


def reverse_words(s: str) -> str:
    # this is O(n) in time, and currently O(n) in space, although I can probably lower that with the cost of readability
    if not s:
        return ''

    rev_s: str = s[::-1]
    rev_s_split = rev_s.split()
    res = []
    for one_word in rev_s_split:
        res.append(one_word[::-1])
    return ' '.join(res)


assert reverse_words('') == ''
assert reverse_words('a') == 'a'
assert reverse_words('hello word here') == 'here word hello'


def reverse_words_extreme(s: str) -> str:
    return ' '.join([x[::-1] for x in s[::-1].split()])


assert reverse_words_extreme('hello word here') == 'here word hello'
