# This problem was asked by Facebook.
#
# Given a string and a set of delimiters, reverse the words in the string while maintaining the relative order of the delimiters. For example, given "hello/world:here", return "here/world:hello"
#
# Follow-up: Does your solution work for the following cases: "hello/world:here/", "hello//world:here"


"""
Similar to reverse words in a string, but this one requires the splitter be preserved.

hello//world:here -> here//world:hello

Maybe I can solve this with two pointers?

Create two array a slow and fast ptr, the fast one scan ahead til it's different from the slow, and stores the substring
in either the word array or the delimiter array.

At the end, combine the two array, keeping the delimiter array in order, while reversing the words

This should be O(n) in time, and O(n) in space

I guess we can assume the string will always begin and ends with words?

"""


def reverse_words(s: str, delimiters: str) -> str:
    if not s or not delimiters:
        return ''

    words = []
    symbols = []
    n = len(s)

    l_ptr, r_ptr = 0, 0 # l_ptr will be inclusive, r_ptr exclusive for sub-stringing

    while l_ptr < n:
        while r_ptr < n and (s[r_ptr].isalpha() == s[l_ptr].isalpha()):
            r_ptr += 1

        if s[l_ptr].isalpha():
            words.append(s[l_ptr: r_ptr])
        else:
            symbols.append(s[l_ptr: r_ptr])

        l_ptr = r_ptr

    words.reverse()
    res = [words[0]]
    i = 0
    for one_symbol in symbols:
        res.append(one_symbol)
        res.append(words[i + 1]) # assuming words are always one more than symbol blocks
        i += 1

    return "".join(res)


assert reverse_words("hello", "/") == 'hello'
assert reverse_words("hello//world:here", "/:") == 'here//world:hello'

