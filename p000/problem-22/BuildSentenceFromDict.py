# This problem was asked by Microsoft.
#
# Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a
# list. If there is more than one possible reconstruction, return any of them. If there is no possible
# reconstruction, then return null.
#
# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should
# return ['the', 'quick', 'brown', 'fox'].
#
# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either
# ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

def build_sentence(s: str, word_bank: set):
    # this should be O(n)
    if not s or not word_bank:
        return None

    idx = 0
    sentence = []
    while idx < len(s):
        walker = idx + 1
        while walker < len(s):
            word = s[idx:walker+1]  # important! I want the word on both boundaries, and this is always within len(s)
            if word in word_bank:
                sentence.append(word)
                idx = walker
                # found a word, move starting idx to end of current word, then break out to outer most loop
                break
            walker += 1
        idx += 1
    return sentence


assert build_sentence("", set([])) is None
assert build_sentence("ok", {'ok'}) == ['ok'], "actual output: {}".format(build_sentence("ok", {'ok'}))
assert build_sentence("thequickbrownfox", {'the', 'quick', 'brown', 'fox'}) == ['the', 'quick', 'brown', 'fox'], \
    'actual output: {}'.format(build_sentence("thequickbrownfox", {'the', 'quick', 'brown', 'fox'}))
assert build_sentence('bedbathandbeyond', {'bed', 'bath', 'and', 'beyond'}) == ['bed', 'bath', 'and', 'beyond'], \
    'actual output: {}'.format(build_sentence('bedbathandbeyond', {'bed', 'bath', 'and', 'beyond'}))
