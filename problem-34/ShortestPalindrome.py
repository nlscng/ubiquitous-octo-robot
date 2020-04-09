# This problem was asked by Quora.
#
# Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible
# anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the
# lexicographically earliest one (the first one alphabetically).
#
# For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is
# the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding
# three letters, but "ecarace" comes first alphabetically.
#
# As another example, given the string "google", you should return "elgoogle".

def is_palindrome(test_word: str):
    # utility function to test if a word is a palindrome
    if not test_word or not isinstance(test_word, str):
        return False
    b_walker, e_walker = 0, len(test_word) - 1
    while b_walker < e_walker:
        b = test_word[b_walker]
        e = test_word[e_walker]
        if b != e:
            return False
        b_walker += 1
        e_walker -= 1
    return True


assert is_palindrome("a")
assert not is_palindrome("")
assert is_palindrome("aba")


def build_next_words(word_set: set, new_char, valid_word: str):
    found = set()
    for word in list(word_set):
        new_word = new_char + word + new_char
        if valid_word in new_word:
            found.add(new_word)
    return found


def shortest_palindrome(word: str):
    # let P(i, j) be the set of shortest possible palidrome that is using at least w_i, ... w_j, where i and j are
    # indices to the given word.
    # then P(i, j) is:
    # if word[i:j+1] is itself a palindrome, word[i:j+1],
    # or, union of (palindrome build from P(i, j-1) + word[j]) and (palindrome build from P(i+1, j) + word[i])

    # essentially we are two walkers walking inwards from the edges of the given word
    if not word or not isinstance(word, str):
        return ""

    n = len(word)
    memo = [[set() for _ in range(n)] for _ in range(n)]
    for i in range(n):
        memo[i][i].add(word[i])

    # build palindrome given each individual char in the str
    for width in range(1, n):
        for i in range(n - width):
            j = i + width
            cell_self = word[i:j + 1]
            if is_palindrome(cell_self):
                memo[i][j] = {cell_self}
            else:
                from_left = build_next_words(memo[i][j - 1], word[j], word[i:j + 1])
                from_down = build_next_words(memo[i + 1][j], word[i], word[i:j + 1])
                memo[i][j] = from_left.union(from_down)

    found = list(memo[0][n - 1])
    found.sort(key=lambda one_word: (len(one_word), one_word))

    return found[0]


assert shortest_palindrome("") == ""
assert shortest_palindrome("a") == "a"
assert shortest_palindrome("aa") == "aa"
assert shortest_palindrome("ab") == "aba"
assert shortest_palindrome("abb") == "abba"
assert shortest_palindrome("aab") == "baab"
assert shortest_palindrome("racecar") == "racecar"
assert shortest_palindrome("google") == "elgoogle"
assert shortest_palindrome("elgoog") == "elgoogle"
assert shortest_palindrome("race") == "ecarace"
