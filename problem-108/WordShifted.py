# This problem was asked by Google.
#
# Given two strings A and B, return whether or not A can be shifted some number of times to get B.
#
# For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.


'''
two pointers
abcde
  *
  cdeab
  *

aaaa
*
  aaab
  *
O(n * m) worst case


double one of them and search for the other?
abcdeabcde
  cdeab

this is linear
'''


# GG: tricky to move away from naive solution, but once you see the double-n-search idea, this is simple
def word_shifted(word_a: str, word_b: str) -> bool:
    if not word_a or not word_b or (len(word_a) != len(word_b)):
        return False

    double_a = word_a + word_a
    return word_b in double_a


assert word_shifted('abcde', 'cdeab')
