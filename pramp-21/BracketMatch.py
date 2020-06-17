# A string of brackets is considered correctly matched if every opening bracket in the string can be paired up with a
# later closing bracket, and vice versa. For instance, “(())()” is correctly matched, whereas “)(“ and “((” aren’t.
# For instance, “((” could become correctly matched by adding two closing brackets at the end, so you’d return 2.
#
# Given a string that consists of brackets, write a function bracketMatch that takes a bracket string as an input and
# returns the minimum number of brackets you’d need to add to the input in order to make it correctly matched.
#
# Explain the correctness of your code, and analyze its time and space complexities.
#
# Examples:
#
# input:  text = “(()”
# output: 1
#
# input:  text = “(())”
# output: 0
#
# input:  text = “())(”
# output: 2


def bracket_match(text: str) -> int:
    # GG: I froze on this problem, starting out thinking a stack-ish solution
    #  moved on to scanning, but can't figure out the pattern. Trick is, a closing paren
    #  can't be balanced by any open paren on the right
    if not text or len(text) == 1:
        return len(text)

    cur_open = 0
    unbalanced_close = 0
    for c in text:
        if cur_open > 0:
            if c == '(':
                cur_open += 1
            else:
                cur_open -= 1
        else:
            if c == '(':
                cur_open += 1
            else:
                unbalanced_close += 1

    return cur_open + unbalanced_close


assert bracket_match('(()') == 1
assert bracket_match('(())') == 0
assert bracket_match('())(') == 2
