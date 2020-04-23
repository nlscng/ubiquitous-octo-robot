# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (
# well-formed).
#
# For example, given the string "([])[]({})", you should return true.
#
# Given the string "([)]" or "((()", you should return false.
#


def is_balanced(brackets: str) -> bool:
    if not isinstance(brackets, str):
        raise Exception("Expcted a string, got {} instead.".format(type(brackets)))

    if len(brackets) == 0:
        return True

    stack = []

    for b in brackets:
        peek = "" if len(stack) == 0 else stack[-1]
        if peek == '{' and b == '}' or \
                (peek == '<' and b == '>') or \
                (peek == '(' and b == ')') or \
                (peek == '[' and b == ']'):
            stack.pop()
        else:
            stack.append(b)

    return len(stack) == 0


assert is_balanced('')
assert not is_balanced('([)]')
assert is_balanced('([])[]({})')
